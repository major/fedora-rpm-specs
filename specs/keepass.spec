Name:           keepass
Version:        2.59
Release:        %autorelease
Summary:        Password manager

License:        GPL-2.0-or-later
URL:            https://keepass.info/

Source0:        https://downloads.sourceforge.net/project/%{name}/KeePass%202.x/%{version}/KeePass-%{version}-Source.zip
Source1:        https://keepass.info/integrity/v2/KeePass-%{version}-Source.zip.asc
Source2:        https://keepass.info/integrity/DominikReichl.asc
Source3:        %{name}.appdata.xml

# Upstream does not include a .desktop file, etc..
Patch0:         keepass-desktop-integration.patch

# Move XSL files to /usr/share/keepass:
Patch1:         keepass-fix-XSL-search-path.patch

ExclusiveArch:  %{mono_arches}
ExcludeArch:    armv7hl
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  gnupg2
BuildRequires:  libappstream-glib
BuildRequires:  libgdiplus-devel
BuildRequires:  mono-devel
BuildRequires:  mono-winforms
BuildRequires:  mono-web
BuildRequires:  xorg-x11-server-Xvfb
Requires:       xdotool xsel hicolor-icon-theme
Requires:       mono-winforms
Recommends:     libargon2
%if 0%{?fedora} >=24 || 0%{?rhel} >= 8
Recommends:     libgcrypt
%endif


# The debuginfo package would be empty if created.
%global debug_package %{nil}


%description
KeePass is a free open source password manager, which helps you to
remember your passwords in a secure way. You can put all your passwords in
one database, which is locked with one master key or a key file.  You
only have to remember one single master password or select the key file
to unlock the whole database.


%prep
%{gpgverify}                \
  --keyring='%{SOURCE2}'    \
  --signature='%{SOURCE1}'  \
  --data='%{SOURCE0}'

%autosetup -p1 -c

# use /app prefix in flatpak builds
%if 0%{?flatpak}
sed -i -e 's|/usr|%{_prefix}|g' dist/%{name} KeePass/App/AppDefs.cs
%endif

# Make sure no prebuilt dlls are shipped
find -name "*dll" -delete

# Work around libpng bug (https://bugzilla.redhat.com/show_bug.cgi?id=1276843):
find -name \*.png -print0 | xargs -0 mogrify -define png:format=png32


%build
( cd Build && sh PrepMonoDev.sh )
find . -name "*.sln" -print -exec sed -i 's/Format Version 10.00/Format Version 11.00/g' {} \;
xbuild /target:KeePass /property:TargetFrameworkVersion=v$(ls -d %{_monodir}/*-api | cut -d/ -f5 | cut -d- -f1 | sort -Vr | head -1) /property:Configuration=Release KeePass.sln
for subdir in Images_App_HighRes Images_Client_16 Images_Client_HighRes; do
    xvfb-run -a mono Build/KeePass/Release/KeePass.exe -d:`pwd`/Ext/$subdir --makexspfile `pwd`/KeePass/Resources/Data/$subdir.bin
done
xbuild /target:KeePass /property:TargetFrameworkVersion=v$(ls -d %{_monodir}/*-api | cut -d/ -f5 | cut -d- -f1 | sort -Vr | head -1) /property:Configuration=Release KeePass.sln

%install
install -d %{buildroot}/%{_prefix}/lib/%{name} %{buildroot}/%{_prefix}/lib/%{name}/Languages %{buildroot}/%{_datadir}/%{name} %{buildroot}/%{_datadir}/%{name}/XSL %{buildroot}/%{_datadir}/applications %{buildroot}/%{_bindir} %{buildroot}/%{_datadir}/mime/packages %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps %{buildroot}/%{_datadir}/icons/hicolor/16x16/apps %{buildroot}/%{_mandir}/man1 %{buildroot}/%{_docdir}/%{name} %{buildroot}/%{_datadir}/appdata
install -p -m 0644 Build/KeePass/Release/KeePass.exe Ext/KeePass.config.xml Ext/KeePass.exe.config %{buildroot}/%{_prefix}/lib/%{name}
install -p -m 0644 Ext/XSL/KDBX_Common.xsl Ext/XSL/KDBX_DetailsFull_HTML.xsl Ext/XSL/KDBX_DetailsLight_HTML.xsl Ext/XSL/KDBX_PasswordsOnly_TXT.xsl Ext/XSL/KDBX_Tabular_HTML.xsl %{buildroot}/%{_datadir}/%{name}/XSL
install -p -m 0644 -T Ext/Icons_15_VA/KeePass_Round/KeePass_Round_512.png %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
install -p -m 0644 -T Ext/Icons_15_VA/KeePass_Round/KeePass_Round_256.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
install -p -m 0644 -T Ext/Icons_15_VA/KeePass_Round/KeePass_Round_128.png %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -p -m 0644 -T Ext/Icons_15_VA/KeePass_Round/KeePass_Round_64.png %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -p -m 0644 -T Ext/Icons_15_VA/KeePass_Round/KeePass_Round_48.png %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -p -m 0644 -T Ext/Icons_15_VA/KeePass_Round/KeePass_Round_32.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -p -m 0644 -T Ext/Icons_15_VA/KeePass_Round/KeePass_Round_16.png %{buildroot}/%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
desktop-file-install --dir=%{buildroot}/%{_datadir}/applications dist/%{name}.desktop
install -p -m 0644 dist/%{name}.xml %{buildroot}/%{_datadir}/mime/packages
install -p -m 0644 dist/%{name}.1 %{buildroot}/%{_mandir}/man1
install -p -m 0644 %{SOURCE3} %{buildroot}/%{_datadir}/appdata
install -p dist/%{name} %{buildroot}/%{_bindir}
sed 's/\r$//' Docs/History.txt > %{buildroot}/%{_docdir}/%{name}/History.txt
sed 's/\r$//' Docs/License.txt > %{buildroot}/%{_docdir}/%{name}/License.txt


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml


%files
%doc %{_docdir}/%{name}/History.txt
%license %{_docdir}/%{name}/License.txt
%{_bindir}/%{name}
%{_prefix}/lib/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_mandir}/man1/%{name}.1*
%{_datadir}/appdata/%{name}.appdata.xml


%changelog
%autochangelog
