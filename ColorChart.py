import skia
import numpy as np


class BaseColors:
    """Color base class"""
    def __init__(self):
        return

    def __del__(self):
        return


class sRGBColors(BaseColors):
    """sRGB color class"""
    MatSRGB = [
        np.matrix(dtype=int, data=[115, 82, 68]),
        np.matrix(dtype=int, data=[194, 150, 130]),
        np.matrix(dtype=int, data=[98, 122, 157]),
        np.matrix(dtype=int, data=[87, 108, 67]),
        np.matrix(dtype=int, data=[133, 128 ,177]),
        np.matrix(dtype=int, data=[103, 189, 170]),

        np.matrix(dtype=int, data=[214, 126, 44]),
        np.matrix(dtype=int, data=[80, 91, 166]),
        np.matrix(dtype=int, data=[193, 90, 99]),
        np.matrix(dtype=int, data=[94 ,60, 108]),
        np.matrix(dtype=int, data=[157, 188, 64]),
        np.matrix(dtype=int, data=[224, 163, 46]),

        np.matrix(dtype=int, data=[56, 61, 150]),
        np.matrix(dtype=int, data=[70, 148, 73]),
        np.matrix(dtype=int, data=[175, 54, 60]),
        np.matrix(dtype=int, data=[231, 199, 31]),
        np.matrix(dtype=int, data=[187, 86, 149]),
        np.matrix(dtype=int, data=[  8, 133, 161]),

        np.matrix(dtype=int, data=[243, 243, 242]),
        np.matrix(dtype=int, data=[200, 200, 200]),
        np.matrix(dtype=int, data=[160, 160, 160]),
        np.matrix(dtype=int, data=[122, 122, 121]),
        np.matrix(dtype=int, data=[85, 85, 85]),
        np.matrix(dtype=int, data=[52, 52, 52]),
    ]   


    def __init__(self):
        super().__init__()
    
    def __del__(self):
        return

    def func(self, arg):
        print(arg)


class ColorChart:
    Width = 1500
    Height = 900
    Margin = 16
    Column = 6
    Row    = 4

    def __init__(self):
        return

    def Create(self, sRGB_color_list):
        assert len(sRGB_color_list) == ColorChart.Column * ColorChart.Row

        surface = skia.Surface(ColorChart.Width, ColorChart.Height)
        with surface as canvas:
            rect = skia.Rect(0, 0, ColorChart.Width, ColorChart.Height)
            paint = skia.Paint(Color=skia.ColorBLACK, Style=skia.Paint.kFill_Style)
            canvas.drawRect(rect, paint)
            
            chart_idx = 0
            w = ColorChart.Width - ColorChart.Margin
            h = ColorChart.Height - ColorChart.Margin
            for r in range(ColorChart.Row):
                for c in range(ColorChart.Column):
                    x = w / ColorChart.Column * c
                    y = h / ColorChart.Row * r
                    rect = skia.Rect(
                        ColorChart.Margin + x, 
                        ColorChart.Margin + y,
                        ColorChart.Margin + x + (w / ColorChart.Column - ColorChart.Margin),
                        ColorChart.Margin + y + (h / ColorChart.Row - ColorChart.Margin))

                    rgb_color = sRGB_color_list[chart_idx];
                    
                    paint = skia.Paint(
                        Color=skia.ColorSetRGB(rgb_color[0,0], rgb_color[0,1], rgb_color[0,2]),
                        Style=skia.Paint.kFill_Style)
                    
                    canvas.drawRect(rect, paint)
                    chart_idx+=1
        
            image = surface.makeImageSnapshot()
            image.save('output.png', skia.kPNG)
        return


chart = ColorChart()
chart.Create(sRGBColors.MatSRGB)
