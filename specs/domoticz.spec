#global git_short_hash df9de70
#global git_hash df9de7020c4317a484c39f7330e6d1c9ca3d9ec9

Name:		domoticz
Version:	2024.7
Release:	3%{?dist}
Summary:	Open source Home Automation System

# Automatically converted from old format: GPLv3+ and ASL 2.0 and Boost and BSD and MIT - review is highly recommended.
License:	GPL-3.0-or-later AND Apache-2.0 AND BSL-1.0 AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:		http://www.domoticz.com
Source0:	https://github.com/domoticz/domoticz/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Source0:	https://github.com/domoticz/domoticz/archive/%%{git_short_hash}.tar.gz#/%%{name}-%%{version}.tar.gz
Source1:	%{name}.service
Source2:	%{name}.conf
# Manually update version reported inside app
Source3:	%{name}-appversion

# Use system tinyxpath (https://github.com/domoticz/domoticz/pull/1759)
Patch1:		%{name}-tinyxpath.patch
# Fix python detection (https://github.com/domoticz/domoticz/pull/1749)
Patch2:		%{name}-python.patch
# Python linking fix
Patch3:		%{name}-python-link.patch

BuildRequires:	boost-devel
BuildRequires:	cereal-devel
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	fmt-devel
BuildRequires:	fontpackages-devel
BuildRequires:	gcc-c++
BuildRequires:	git
BuildRequires:	jsoncpp-devel
BuildRequires:	libopenzwave-devel >= 1.6.0
BuildRequires:	lua-devel
BuildRequires:	make
BuildRequires:	minizip-compat-devel
BuildRequires:	mosquitto-devel
BuildRequires:	openssl-devel
BuildRequires:	python3-devel
BuildRequires:	sqlite-devel
BuildRequires:	systemd-devel
BuildRequires:	tinyxpath-devel
BuildRequires:	zlib-devel

Requires(pre):	shadow-utils
Requires(post):	systemd
Requires(postun):	systemd
Requires(preun):	systemd

Requires:	google-droid-sans-fonts
Recommends:     mosquitto
Recommends:	system-python-libs >= 3.4
#Recommends:     zwave-js-ui

Provides:	bundled(js-ace)
Provides:	bundled(js-angularamd) = 0.2.1
Provides:	bundled(js-angularjs) = 1.5.8
Provides:	bundled(js-blockly)
Provides:	bundled(js-bootbox)
Provides:	bundled(js-bootstrap) = 3.2.0
Provides:	bundled(js-colpick)
Provides:	bundled(js-d3)
Provides:	bundled(js-datatables-datatools) = 2.2.3
Provides:	bundled(js-dateformat) = 1.2.3
Provides:	bundled(js-filesaver) = 0.0-git20140725
Provides:	bundled(js-highcharts) = 4.2.6
Provides:	bundled(js-html5shiv) = 3.6.2
Provides:	bundled(js-i18next) = 1.8.0
Provides:	bundled(js-jquery) = 1.12.0
Provides:	bundled(js-ngdraggable)
Provides:	bundled(js-nggrid)
Provides:	bundled(js-jquery-noty) = 2.1.0
Provides:	bundled(js-require) = 2.1.14
Provides:	bundled(js-respond) = 1.1.0
Provides:	bundled(js-angular-ui-bootstrap) = 0.13.4
Provides:	bundled(js-wow) = 0.1.9
Provides:	bundled(js-ozwcp)
Provides:	bundled(js-less) = 1.3.0
Provides:	bundled(js-ion-sound) = 3.0.6
Provides:	bundled(js-zeroclipboard) = 1.0.4

%global _python_bytecompile_extra 0


%description
Domoticz is a Home Automation System that lets you monitor and configure various
devices like: Lights, Switches, various sensors/meters like Temperature, Rain,
Wind, UV, Electra, Gas, Water and much more. Notifications/Alerts can be sent to
any mobile device


%prep
%setup -q -n %{name}-%{version}
#setup -q -n %{name}-%{git_hash}
%patch -P 1 -p1 -b.tinyxpath
%patch -P 2 -p1 -b.python
%patch -P 3 -p1 -b.python-link
# Add support for future versions of Python by replacing hardcoded version with macro
sed -i 's/-lpythonVER/-lpython%{python3_version}/' CMakeLists.txt
# Renaming of old define used wrong case in ZWave file
sed -i 's/sTypeSetPoint/sTypeSetpoint/g' hardware/ZWaveBase.cpp
rm -rf sqlite/
rm -rf tinyxpath/
cp -p %{SOURCE3} ./appversion.h


%build
%cmake \
 -DCMAKE_BUILD_TYPE=RelWithDebInfo \
 -DUSE_STATIC_LIBSTDCXX=NO \
 -DUSE_STATIC_OPENZWAVE=NO \
 -DUSE_OPENSSL_STATIC=NO \
 -DUSE_BUILTIN_JSONCPP=NO \
 -DUSE_BUILTIN_LIBFMT=NO \
 -DUSE_BUILTIN_LUA=NO \
 -DUSE_BUILTIN_MINIZIP=NO \
 -DUSE_BUILTIN_MQTT=NO \
 -DUSE_BUILTIN_SQLITE=NO \
 -DUSE_BUILTIN_TINYXPATH=NO \
 -DUSE_STATIC_BOOST=NO \
 -DCMAKE_INSTALL_PREFIX=%{_datadir}/%{name} \
 %{nil}
%cmake_build


%install
%cmake_install

# remove bundled OpenZWave configuration files so system files are used
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/Config/

# remove docs, we grab them in files below
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/*.txt

# move binary to standard directory
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name} $RPM_BUILD_ROOT%{_bindir}/

# install systemd service and config
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/
mkdir -p $RPM_BUILD_ROOT%{_unitdir}/
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}

# create backups/database/plugins/scripts/ssl cert directory
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/{backups,plugins,scripts,templates}
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/{dzVents,lua,lua_parsers,python,templates}
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/dzVents/{data,generated_scripts,scripts}

# Disable the app's self-update script
chmod 644 $RPM_BUILD_ROOT%{_datadir}/%{name}/updatedomo

# Unbundle DroidSans.ttf
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/www/styles/elemental/fonts/DroidSans.ttf
ln -s %{_fontdir}/google-droid/DroidSans.ttf \
      $RPM_BUILD_ROOT%{_datadir}/%{name}/www/styles/elemental/fonts/
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/www/styles/element-light/fonts/DroidSans.ttf
ln -s %{_fontdir}/google-droid/DroidSans.ttf \
      $RPM_BUILD_ROOT%{_datadir}/%{name}/www/styles/element-light/fonts/
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/www/styles/element-dark/fonts/DroidSans.ttf
ln -s %{_fontdir}/google-droid/DroidSans.ttf \
      $RPM_BUILD_ROOT%{_datadir}/%{name}/www/styles/element-dark/fonts/

# Link default plugins and scripts to userdata directory
ln -s %{_datadir}/%{name}/scripts/dzVents/data/README.md \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/dzVents/data/README.md
ln -s %{_datadir}/%{name}/scripts/dzVents/generated_scripts/README.md \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/dzVents/generated_scripts/README.md
ln -s %{_datadir}/%{name}/scripts/dzVents/scripts/README.md \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/dzVents/scripts/README.md
ln -s %{_datadir}/%{name}/scripts/templates/All.{dzVents,Lua,Python} \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/Bare.dzVents \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/Device.{dzVents,Lua} \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/global_data.dzVents \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/Group.dzVents \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/HTTPRequest.dzVents \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/Scene.dzVents \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/Security.{dzVents,Lua} \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/Time.Lua \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/Timer.dzVents \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/
ln -s %{_datadir}/%{name}/scripts/templates/UserVariable.{dzVents,Lua} \
      $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/scripts/templates/

# Link web page templates to userdata directory
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/www/templates/{custom.example,readme.txt} \
   $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}/templates
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/www/templates
ln -s %{_sharedstatedir}/%{name}/templates \
      $RPM_BUILD_ROOT%{_datadir}/%{name}/www/templates

# Byte compile the default plugin
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/%{name}/plugins/AwoxSMP


%pretrans
# Handle directory move for a few releases
rm -rf %{_datadir}/%{name}/www/templates


%pre
getent group domoticz >/dev/null || groupadd -r domoticz
getent passwd domoticz >/dev/null || \
useradd -r -g domoticz -d %{_datadir}/%{name} -s /sbin/nologin \
-c "Domoticz Home Automation Server" domoticz
# For OpenZWave USB access (/dev/ttyACM#)
usermod -G domoticz,dialout domoticz


%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%files
%license License.txt
%doc README.md History.txt
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_datadir}/%{name}/
%attr(0755,domoticz,domoticz) %{_sharedstatedir}/%{name}/
%{_unitdir}/%{name}.service


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2024.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Jan 05 2025 Michael Cronenworth <mike@cchtml.com> - 2024.7-2
- Fix ZWave SetPoint devices

* Fri Dec 27 2024 Michael Cronenworth <mike@cchtml.com> - 2024.7-1
- New stable release

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2023.2-7
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 2023.2-3
- Rebuilt for Boost 1.83

* Mon Dec 04 2023 Lukas Javorsky <ljavorsk@redhat.com> - 2023.2-2
- Rebuilt for minizip-ng transition Fedora change
- Fedora Change: https://fedoraproject.org/wiki/Changes/MinizipNGTransition

* Fri Nov 10 2023 Michael Cronenworth <mike@cchtml.com> - 2023.2-1
- New stable release

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 01 2023 Python Maint <python-maint@redhat.com> - 2022.1-10
- Rebuilt for Python 3.12

* Wed Jun 28 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2022.1-9
- Rebuilt due to fmt 10 update.

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 2022.1-8
- Rebuilt for Python 3.12

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 2022.1-7
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 25 2022 Michael Cronenworth <mike@cchtml.com> - 2022.1-5
- Python 3.11 support (RHBZ#2093917)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2022.1-3
- Rebuilt for Python 3.11

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 2022.1-2
- Rebuilt for Boost 1.78

* Fri Mar 11 2022 Michael Cronenworth <mike@cchtml.com> - 2022.1-1
- New stable release

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 05 2022 Michael Cronenworth <mike@cchtml.com> - 2021.1-9
- Handle templates directory upgrade path

* Mon Jan 03 2022 Michael Cronenworth <mike@cchtml.com> - 2021.1-8
- Symlink web page templates directory (RHBZ#1975094)

* Thu Dec 16 2021 Michael Cronenworth <mike@cchtml.com> - 2021.1-7
- Add patch for Python 3.10 support

* Wed Nov 03 2021 Björn Esser <besser82@fedoraproject.org> - 2021.1-6
- Rebuild (jsoncpp)

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2021.1-5
- Rebuilt with OpenSSL 3.0.0

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 2021.1-4
- Rebuilt for Boost 1.76

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 05 2021 Richard Shaw <hobbes1069@gmail.com> - 2021.1-2
- Rebuild for new fmt version.

* Sat May 29 2021 Michael Cronenworth <mike@cchtml.com> - 2021.1-1
- New stable release

* Wed Mar 31 2021 Jonathan Wakely <jwakely@redhat.com> - 2020.2-9
- Rebuilt for removed libstdc++ symbols (#1937698)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2020.2-8
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 2020.2-6
- Rebuilt for Boost 1.75

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Michael Cronenworth <mike@cchtml.com> - 2020.2-4
- Rebuild for Boost 1.73 (RHBZ#1843104)

* Sat May 30 2020 Björn Esser <besser82@fedoraproject.org> - 2020.2-3
- Rebuild (jsoncpp)
- Add a patch to fix build with Python 3.9 (RHBZ#1842068)

* Mon Apr 27 2020 Michael Cronenworth <mike@cchtml.com> - 2020.2-2
- Link against older minizip

* Mon Apr 27 2020 Michael Cronenworth <mike@cchtml.com> - 2020.2-1
- New stable release

* Tue Apr 21 2020 Michael Cronenworth <mike@cchtml.com> - 2020.1-2
- Fix dzVents (RHBZ#1759558)

* Tue Mar 24 2020 Michael Cronenworth <mike@cchtml.com> - 2020.1-1
- New stable release

* Wed Feb 05 2020 Michael Cronenworth <mike@cchtml.com> - 4.11671-0.git20200202.1
- Update git checkout

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.11553-0.git20191207.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 07 2019 Michael Cronenworth <mike@cchtml.com> - 4.11553-0.git20191207.1
- Update git checkout (RHBZ#1780739)

* Wed Oct 09 2019 Michael Cronenworth <mike@cchtml.com> - 4.11352-0.git20191006.1
- Update git checkout and fix scripts directories (RHBZ#1759558)

* Sat Aug 31 2019 Michael Cronenworth <mike@cchtml.com> - 4.11250-0.git20190831.1
- Fix app version to match upstream versioning
- Fix default userdata location so the app can write to it

* Sat Aug 31 2019 Michael Cronenworth <mike@cchtml.com> - 4.10718-0.git20190831.1
- Version update to current master git checkout
- Compile against OpenZWave 1.6

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9700-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9700-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 4.9700-5
- Rebuilt for Boost 1.69

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 4.9700-4
- Append curdir to CMake invokation. (#1668512)

* Sun Nov 11 2018 Michael Cronenworth <mike@cchtml.com> - 4.9700-3
- Add patch to support Python 3.7

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.9700-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Michael Cronenworth <mike@cchtml.com> - 4.9700-1
- Version update

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.8153-7
- Rebuilt for Python 3.7

* Mon Jun 18 2018 Michael Cronenworth <mike@cchtml.com> - 3.8153-6
- Do not compile some of the extra Python files
- Add patch to fix bug in OZWCP javascript

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8153-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Michael Cronenworth <mike@cchtml.com> - 3.8153-4
- Add OpenZWave Command Class Barrier support
- Boost 1.66 support (RHBZ#1538585)

* Fri Sep 08 2017 Michael Cronenworth <mike@cchtml.com> - 3.8153-3
- Fix OpenZWave control panel symlink (RHBZ#1482266)
- Fix Python detection

* Mon Jul 31 2017 Michael Cronenworth <mike@cchtml.com> - 3.8153-2
- Fix OpenZWave control panel

* Mon Jul 31 2017 Michael Cronenworth <mike@cchtml.com> - 3.8153-1
- New upstream version
- Unbundle tinyxpath

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5877-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 3.5877-2
- Rebuilt for Boost 1.64

* Wed Jul 19 2017 Michael Cronenworth <mike@cchtml.com> - 3.5877-1
- Initial spec
