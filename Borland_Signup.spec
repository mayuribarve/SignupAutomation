# -*- mode: python -*-

block_cipher = None


a = Analysis(['features\\steps\\borland_signup.py'],
             pathex=['C:\\Users\\mayurib\\PycharmProjects\\BorlandTesting\\SignupAutomation'],
             binaries=[],
             datas=[('AutomationTestData.xlsx', '.'), ('environment.py', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='Borland_Signup',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Borland_Signup')
