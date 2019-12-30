# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys #需要引入 keys 包
import requests
from PIL import Image
from six import BytesIO
import time
import random
import matplotlib.pyplot as plt

class Actions(ActionChains):
    def wait(self, time_s:float):
        self._actions.append(lambda: time.sleep(time_s))
        return self

        
def verify(browser):
    
    browser.execute_script("window.scrollBy(0,-900)")
    slice_img_label = browser.find_element_by_css_selector('div.geetest_slicebg') #找到滑动图片标签
    browser.execute_script("document.getElementsByClassName('geetest_canvas_slice')[0].style['display'] = 'none'") #将小块隐藏
    full_img_label = browser.find_element_by_css_selector('canvas.geetest_canvas_fullbg') #原始图片的标签
    position = get_position(slice_img_label) #获取滑动验证图片的位置，此函数的定义在第4点
    screenshot_slice = get_screenshot(browser) # 截取整个浏览器图片，此函数的定义在第5点"""
    position_scale = get_position_scale(browser,screenshot_slice) #获取截取图片宽高和浏览器宽高的比例，此函数的定义在第6点
    slice_img = get_slideimg_screenshot(screenshot_slice,position,position_scale) #截取有缺口的滑动验证图片，此函数的定义在第7点
    browser.execute_script("document.getElementsByClassName('geetest_canvas_fullbg')[0].style['display'] = 'block'") #在浏览器中显示原图
    screenshot_full = get_screenshot(browser) #获取整个浏览器图片
    position = get_position(full_img_label)## alex add try
    full_img = get_slideimg_screenshot(screenshot_full,position,position_scale) # 截取滑动验证原图
    browser.execute_script("document.getElementsByClassName('geetest_canvas_slice')[0].style['display'] = 'block'")  #将小块重新显示
    left = compare(full_img,slice_img) #将原图与有缺口图片进行比对，获得缺口的最左端的位置，此函数定义在第8点
    print("left:",left)
    print("position_scale[0]:",position_scale[0])
    left = left / position_scale[0] #将该位置还原为浏览器中的位置

    slide_btn = browser.find_element_by_css_selector('.geetest_slider_button') #获取滑动按钮
    track = get_track(left) #获取滑动的轨迹，此函数定义在第9点
    move_to_gap(browser,slide_btn,track) #进行滑动，此函数定义在第10点"""
    
    #success = browser.find_element_by_css_selector('.geetest_success_radar_tip') #获取显示结果的标签
    #time.sleep(2)
    #if success.text == "验证成功":
    #    print(success.text)
    #    print('成功')
        #login_btn = browser.find_element_by_css_selector('button.j-login-btn') #如果验证成功，则点击登录按钮
        #login_btn.click()
    #else:
    #    print(success.text)
    #    print('失败') 

def get_position(img_label):
    location = img_label.location
    size = img_label.size
    top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
        'width']
    print(left,top,right,bottom)
    return (left, top, right, bottom)

def get_screenshot(browser):
    screenshot = browser.get_screenshot_as_png()
    f = BytesIO()
    f.write(screenshot)
    #image = Image.open(f)
    #plt.imshow(image)
    #plt.show()
    return Image.open(f)

def get_position_scale(browser,screen_shot):
    height = browser.execute_script('return document.documentElement.clientHeight')
    width = browser.execute_script('return document.documentElement.clientWidth')
    x_scale = screen_shot.size[0] / (width+10)
    y_scale = screen_shot.size[1] / (height)
    return (x_scale,y_scale)

def get_slideimg_screenshot(screenshot,position,scale):
    x_scale,y_scale = scale
    x = position[2]-position[0]
    y = position[3]-position[1]
    #plt.imshow(screenshot)
    #plt.show()

    print("x_scale:",x_scale,"y_scale:",y_scale)
    #position = [position[0]/x_scale, position[1]/y_scale, position[2]/x_scale, position[3]/y_scale]
    #position = [position[0], position[1], position[0]+x/x_scale, position[1]+y/y_scale]
    position = [position[0]*x_scale+10,(position[1])*y_scale,position[0]*x_scale+x*x_scale,(position[1])*y_scale+y*y_scale]
    screenshotpo = screenshot.crop(position)
    #plt.imshow(screenshotpo)
    #plt.show()
    return screenshotpo

def compare_pixel(img1,img2,x,y):
    pixel1 = img1.load()[x,y]
    pixel2 = img2.load()[x,y]
    threshold = 50
    if ((abs(pixel1[0]-pixel2[0])<=threshold)and(abs(pixel1[1]-pixel2[1])<=threshold)and(abs(pixel1[2]-pixel2[2])<=threshold)):
    #if(pixel1 == pixel2):
        #print("same,pixel 1 2")
        return True
    else:
        print("not same,pixel 1 2")
        return False


def compare(full_img,slice_img):
    left = 0
    #plt.imshow(full_img)
    #plt.show()
    plt.imshow(slice_img)
    plt.show()
    print("full_img:",full_img.size[0],"full_img_type:",type(full_img))
    print("slice_img:",slice_img.size[1])
    for i in range(full_img.size[0]):
        for j in range(full_img.size[1]):
            if not compare_pixel(full_img,slice_img,i,j):
                print("compare succeed i:",i)         
                return i
            #else:

                #print("compare failed")
    return left

def get_track(distance):
    """
    根据偏移量获取移动轨迹
    :param distance: 偏移量
    :return: 移动轨迹
    """
    print("distance:",distance)
    # 移动轨迹
    track = []
    # 当前位移
    current = 0
    # 减速阈值
    mid = distance * 3 / 5
    # 计算间隔
    t = 0.2
    # 初速度
    v = 0

    while current < distance:
        if current < mid:
            # 加速度为正 2
            a = random.randint(18,22)
            
        else:
            # 加速度为负 3
            a = -30
        # 初速度 v0
        v0 = v
        # 当前速度 v = v0 + at
        v = v0 + a * t
        # 移动距离 x = v0t + 1/2 * a * t^2
        move = v0 * t + 1 / 2 * a * t * t
        # 当前位移
        current += move
        # 加入轨迹
        track.append(round(move))
    return track

def move_to_gap(browser,slider, tracks):
    """
    拖动滑块到缺口处
    :param slider: 滑块
    :param tracks: 轨迹
    :return:
    """

    # step 设置步调的长度
    action = Actions(browser)
    action.click_and_hold(slider)
    step = random.randint(2, 4)
    print("step:", step)
    print("tracks:",tracks)
    for x in tracks:
        action.move_by_offset(xoffset=x, yoffset=0)
        action.wait(random.uniform(0.0005, 0.01))
    action.release()
    action.perform()
    time.sleep(8)