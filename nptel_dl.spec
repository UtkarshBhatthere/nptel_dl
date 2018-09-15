# -*- mode: python -*-
a = Analysis(['nptel_dl.py'],
             pathex=['/home/utkarshbhatt/Desktop/Testing/Python/nptel_dl'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='nptel_dl',
          debug=False,
          strip=None,
          upx=True,
          console=True )
