# 创建者：wzz
# 开发时间：2022/4/28 20:18

import numpy as np  # 数据处理用
# import xarray as xr
import matplotlib.pyplot as plt  # 画图用
import cartopy.crs as ccrs  # 投影用
# import cartopy.feature as cfeature
import salem as sl  # 数据处理用


if __name__ == '__main__':
    data = sl.open_wrf_dataset(r'E:\Work\station\MID\exp1-gaungzhou\data\wrfout_d02_2022-03-30_06_00_00.nc')
    # print(data)

    datau500 = data.salem.wrf_plevel('U', levels=500)
    datav500 = data.salem.wrf_plevel('V', levels=500)
    datag500 = data.salem.wrf_plevel('GEOPOTENTIAL', levels=500) / 100
    dataw500 = data.salem.wrf_plevel('QVAPOR', levels=500)
    datat500 = data.salem.wrf_plevel('TK', levels=500) - 273.15

    datau850 = data.salem.wrf_plevel('U', levels=850)
    datav850 = data.salem.wrf_plevel('V', levels=850)
    datag850 = data.salem.wrf_plevel('GEOPOTENTIAL', levels=850) / 100
    dataw850 = data.salem.wrf_plevel('QVAPOR', levels=850)
    datat850 = data.salem.wrf_plevel('TK', levels=850) - 273.15

    datau700 = data.salem.wrf_plevel('U', levels=700)
    datav700 = data.salem.wrf_plevel('V', levels=700)
    datag700 = data.salem.wrf_plevel('GEOPOTENTIAL', levels=700) / 100
    dataw700 = data.salem.wrf_plevel('QVAPOR', levels=700)
    datat700 = data.salem.wrf_plevel('TK', levels=700) - 273.15

    datau925 = data.salem.wrf_plevel('U', levels=925)
    datav925 = data.salem.wrf_plevel('V', levels=925)
    datag925 = data.salem.wrf_plevel('GEOPOTENTIAL', levels=925) / 100
    dataw925 = data.salem.wrf_plevel('QVAPOR', levels=925)
    datat925 = data.salem.wrf_plevel('TK', levels=925) - 273.15

    print('------------500---------------')
    print(datau500.max(), datau500.min())
    print(datag500.max(), datag500.min())
    print(datat500.max(), datat500.min())
    print(dataw500.max(), dataw500.min())

    print('------------700---------------')
    print(datau700.max(), datau700.min())
    print(datag700.max(), datag700.min())
    print(datat700.max(), datat700.min())
    print(dataw700.max(), dataw700.min())

    print('------------850---------------')
    print(datau850.max(), datau850.min())
    print(datag850.max(), datag850.min())
    print(datat850.max(), datat850.min())
    print(dataw850.max(), dataw850.min())

    print('------------925---------------')
    print(datau925.max(), datau925.min())
    print(datag925.max(), datag925.min())
    print(datat925.max(), datat925.min())
    print(dataw925.max(), dataw925.min())

    lat = data['lat'].data
    lon = data['lon'].data
    # print(lat, lon)


    def drawmap():
        fig = plt.figure(figsize=(10, 8))  # 画布大小
        ax = fig.subplots(1, 1, subplot_kw={
            'projection': ccrs.LambertConformal(central_longitude=113.0, central_latitude=22.0, )})  # 画图个数
        ax.coastlines('50m')
        box1 = [106, 118, 16.00, 27.00]
        ax.set_extent(box1, crs=ccrs.PlateCarree())
        ax.gridlines(draw_labels={"bottom": "x", "left": "y"}, color='gray', alpha=0.5,
                     linestyle=':', auto_inline=False, rotate_labels=False)
        return ax, fig


    # ------------------------500hPa绘图----------------------------- #
    ax1, fig1 = drawmap()
    line = ax1.contour(lon[::5, ::5], lat[::5, ::5], datag500[0, ::5, ::5], levels=np.arange(520, 600, 2),
                       colors='blue', transform=ccrs.PlateCarree())
    ax1.clabel(line, inline=True, fontsize=12, fmt='%.0f')
    line = ax1.contour(lon[::5, ::5], lat[::5, ::5], datat500[0, ::5, ::5], levels=np.arange(-11, -4, 1), colors='r',
                       transform=ccrs.PlateCarree())
    ax1.clabel(line, inline=True, fontsize=12, fmt='%.0f')
    colorbar = ax1.contourf(lon[::5, ::5], lat[::5, ::5], dataw500[0, ::5, ::5] * 1000,
                            levels=[0, 1, 2, 3, 4, 5, 6],
                            colors=['#f5f5f5', '#7fff00', '#00ff00', '#00cd00', '#008b00', '#548b54'],
                            transform=ccrs.PlateCarree())
    cb = fig1.colorbar(colorbar, extendrect='True', pad=0.03, fraction=0.1, shrink=0.8)
    cb.ax.set_title('q (g/kg)')
    ax1.quiver(lon[::5, ::5], lat[::5, ::5],
               datau500.loc[np.datetime64('2022-03-30T06:00:00'), ::5, ::5].data,
               datav500.loc[np.datetime64('2022-03-30T06:00:00'), ::5, ::5].data,
               color='k', transform=ccrs.PlateCarree())
    ax1.set_title(
        'Temperature (deg C),   Height (m),  \n Wind (m/s),   q (g/kg)      at 500 hPa',
        fontdict={'fontsize': 11}, loc='left')
    ax1.set_title("Time:" + str(datau500['time'].data[0])[0:19], fontdict={'fontsize': 10}, loc='right')
    plt.savefig('wrf500hPa-gz.png')
    
    # ------------------------850hPa绘图----------------------------- #
    ax2, fig2 = drawmap()
    line = ax2.contour(lon[::5, ::5], lat[::5, ::5], datag850[0, ::5, ::5], levels=np.arange(145, 153, 2),
                       colors='blue', transform=ccrs.PlateCarree())
    ax2.clabel(line, inline=True, fontsize=12, fmt='%.0f')
    line = ax2.contour(lon[::5, ::5], lat[::5, ::5], datat850[0, ::5, ::5], levels=np.arange(7, 23, 2), colors='r',
                       transform=ccrs.PlateCarree())
    ax2.clabel(line, inline=True, fontsize=12, fmt='%.0f')
    colorbar = ax2.contourf(lon[::5, ::5], lat[::5, ::5], dataw850[0, ::5, ::5] * 1000,
                            levels=[6, 7, 8, 9, 10, 11, 12, 13],
                            colors=['#f5f5f5', '#f5f5f5', '#7fff00', '#00ff00',
                                    '#00cd00', '#008b00', '#228b22', '#548b54'],
                            transform=ccrs.PlateCarree())
    cb = fig2.colorbar(colorbar, extendrect='True', pad=0.03, fraction=0.1, shrink=0.8)
    cb.ax.set_title('q (g/kg)')
    ax2.quiver(lon[::5, ::5], lat[::5, ::5],
               datau850.loc[np.datetime64('2022-03-30T06:00:00'), ::5, ::5].data,
               datav850.loc[np.datetime64('2022-03-30T06:00:00'), ::5, ::5].data,
               color='k', transform=ccrs.PlateCarree())
    ax2.set_title(
        'Temperature (deg C),   Height (m),  \n Wind (m/s),   q (g/kg)      at 850 hPa',
        fontdict={'fontsize': 11}, loc='left')
    ax2.set_title("Time:" + str(datau850['time'].data[0])[0:19], fontdict={'fontsize': 10}, loc='right')
    plt.savefig('wrf850hPa-gz.png')

    # ------------------------700hPa绘图----------------------------- #
    ax3, fig3 = drawmap()
    line = ax3.contour(lon[::5, ::5], lat[::5, ::5], datag700[0, ::5, ::5], levels=np.arange(303, 311, 2),
                       colors='blue', transform=ccrs.PlateCarree())
    ax3.clabel(line, inline=True, fontsize=12, fmt='%.0f')
    line = ax3.contour(lon[::5, ::5], lat[::5, ::5], datat700[0, ::5, ::5], levels=np.arange(2, 11, 2), colors='r',
                       transform=ccrs.PlateCarree())
    ax3.clabel(line, inline=True, fontsize=12, fmt='%.0f')
    colorbar = ax3.contourf(lon[::5, ::5], lat[::5, ::5], dataw700[0, ::5, ::5] * 1000,
                            levels=[3, 4, 5, 6, 7, 8, 9, 10],
                            colors=['#f5f5f5', '#f5f5f5', '#7fff00', '#00ff00', '#00cd00',
                                    '#008b00', '#228b22', '#548b54'],
                            transform=ccrs.PlateCarree())
    cb = fig3.colorbar(colorbar, extendrect='True', pad=0.03, fraction=0.1, shrink=0.8)
    cb.ax.set_title('q (g/kg)')
    ax3.quiver(lon[::5, ::5], lat[::5, ::5],
               datau700.loc[np.datetime64('2022-03-30T06:00:00'), ::5, ::5].data,
               datav700.loc[np.datetime64('2022-03-30T06:00:00'), ::5, ::5].data,
               color='k', transform=ccrs.PlateCarree())
    ax3.set_title(
        'Temperature (deg C),   Height (m),  \n Wind (m/s),   q (g/kg)      at 700 hPa',
        fontdict={'fontsize': 11}, loc='left')
    ax3.set_title("Time:" + str(datau850['time'].data[0])[0:19], fontdict={'fontsize': 10}, loc='right')
    plt.savefig('wrf700hPa-gz.png')
    plt.show()

    # ------------------------925hPa绘图----------------------------- #
    ax4, fig4 = drawmap()
    line = ax4.contour(lon[::5, ::5], lat[::5, ::5], datag925[0, ::5, ::5], levels=np.arange(73, 82, 2),
                       colors='blue', transform=ccrs.PlateCarree())
    ax4.clabel(line, inline=True, fontsize=12, fmt='%.0f')
    line = ax4.contour(lon[::5, ::5], lat[::5, ::5], datat925[0, ::5, ::5], levels=np.arange(11, 31, 2), colors='r',
                       transform=ccrs.PlateCarree())
    ax4.clabel(line, inline=True, fontsize=12, fmt='%.0f')
    colorbar = ax4.contourf(lon[::5, ::5], lat[::5, ::5], dataw925[0, ::5, ::5] * 1000,
                            levels=[8, 9, 10, 12, 13, 14, 15, 16],
                            colors=['#f5f5f5', '#f5f5f5', '#7fff00', '#00ff00', '#00cd00',
                                    '#008b00', '#228b22', '#548b54'],
                            transform=ccrs.PlateCarree())
    cb = fig4.colorbar(colorbar, extendrect='True', pad=0.03, fraction=0.1, shrink=0.8)
    cb.ax.set_title('q (g/kg)')
    ax4.quiver(lon[::5, ::5], lat[::5, ::5],
               datau925.loc[np.datetime64('2022-03-30T06:00:00'), ::5, ::5].data,
               datav925.loc[np.datetime64('2022-03-30T06:00:00'), ::5, ::5].data,
               color='k', transform=ccrs.PlateCarree())
    ax4.set_title(
        'Temperature (deg C),   Height (m),  \n Wind (m/s),   q (g/kg)      at 925 hPa',
        fontdict={'fontsize': 11}, loc='left')
    ax4.set_title("Time:" + str(datau850['time'].data[0])[0:19], fontdict={'fontsize': 10}, loc='right')
    plt.savefig('wrf925hPa-gz.png')
    plt.show()
