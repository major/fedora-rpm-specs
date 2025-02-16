%global	urlver		3.5
%global	mainver		3.5.99

%global	core_least_ver	3.5.99

%global	use_git	1
%global	gitdate	20250214
%global	githash	2fabf995462603ec40db60c25d664817fc0fb756
%global	shorthash	%(c=%{githash} ; echo ${c:0:7})

%global	tarballver	%{mainver}%{?use_git:-%{gitdate}git%{shorthash}}

%global	baserelease	1
%global	alphatag		.rc2


%global	ruby_vendorlib	%(ruby -rrbconfig -e "puts RbConfig::CONFIG['vendorlibdir']")

%global	build_unstable	1

%undefine _strict_symbol_defs_build

##########################################
%global		flagrel	%{nil}
%global		use_gcc_strict_sanitize	0

%if	0%{?use_gcc_strict_sanitize} >= 1
%global		flagrel	%{flagrel}.san
%endif
##########################################

Name:			cairo-dock-plug-ins
Version:		%{mainver}%{?use_git:^%{gitdate}git%{shorthash}}
Release:		%{baserelease}%{?alphatag}%{?dist}%{flagrel}
Summary:		Plug-ins files for Cairo-Dock

# SPDX confirmed
License:		GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-2.0-only
URL:			http://glx-dock.org/
#Source0:		http://launchpad.net/cairo-dock-plug-ins/%%{urlver}/%%{mainver}/+download/cairo-dock-plugins-%%{mainver}.tar.gz
# Some contents removed: see https://bugzilla.redhat.com/show_bug.cgi?id=1178912
Source0:		cairo-dock-plugins-fedora-%{tarballver}.tar.gz
# Source0 is created from Source1
Source1:		cairo-dock-plug-ins-create-fedora-tarball.sh
# Port to WebKit2
Patch11:		cairo-dock-plugins-3.4.1-port-WebKit2.patch
# https://fedoraproject.org/wiki/Changes/Remove_webkit2gtk-4.0_API_Version
# Use webkit2gtk-4.1 for F-39+
Patch13:		cairo-dock-plugins-3.4.1-port-WebKit2_gtk41.patch

BuildRequires:  gcc-c++
BuildRequires:	cmake
BuildRequires:	gettext

BuildRequires:	pkgconfig(gldi) = %{core_least_ver}
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gio-2.0)

# Plug-ins
BuildRequires:	pkgconfig(ayatana-indicator3-0.4)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(dbusmenu-glib-0.4)
BuildRequires:	pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(gnome-vfs-2.0)
BuildRequires:	pkgconfig(indicator3-0.4)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libgnome-menu-3.0)
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(libical)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libxklavier)
BuildRequires:	pkgconfig(openssl) >= 1.1
# BuildRequires:	pkgconfig(thunar-vfs-1)
BuildRequires:	pkgconfig(upower-glib)
BuildRequires:	pkgconfig(vte-2.91)
# https://fedoraproject.org/wiki/Changes/Remove_webkit2gtk-4.0_API_Version
# Use webkit2gtk-4.1 for F-39+
BuildRequires:	pkgconfig(webkit2gtk-4.1)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(zeitgeist-2.0)

BuildRequires:	libetpan-devel
BuildRequires:	lm_sensors-devel

# Bindings
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	ruby-devel
BuildRequires:	vala
BuildRequires:	make

Requires:	%{name}-base%{?_isa} = %{version}-%{release}
# Explicitly write below
Requires:	%{name}-dbus%{?_isa} = %{version}-%{release}
# cairo-dock-launcher-API-daemon is written in python,
# so for now make this depending on python
Requires:	cairo-dock-python3%{?_isa} = %{version}-%{release}
# Require xdg-utils for logout by default
Requires:	xdg-utils

%description
This package is a meta package for Cairo-Dock plugins.

%package	base
Summary:	Base files for Cairo-Dock plugins
Requires:	cairo-dock-core%{?_isa} >= %{core_least_ver}
Requires:	%{name}-common = %{version}-%{release}
%if 0%{?fedora} >= 41
Requires:	gdk-pixbuf2-modules-extra
%endif

%description	base
This package contains plug-ins files for Cairo-Dock.


%package	common
Summary:	Common files for Cairo-Dock plugins
BuildArch:	noarch

%description	common
This file contains common files for Cairo-Dock plugins.

%package	dbus
Summary:	Plug-ins files for Cairo-Dock related to Dbus
Requires:	cairo-dock-core%{?_isa} >= %{core_least_ver}
Requires:	%{name}-common = %{version}-%{release}

%description	dbus
This package contains plug-ins files for Cairo-Dock related
to Dbus.

%package	xfce
Summary:	Plug-ins files for Cairo-Dock related to Xfce
Requires:	cairo-dock-core%{?_isa} >= %{core_least_ver}
Requires:	%{name}-common = %{version}-%{release}

%description	xfce
This package contains plug-ins files for Cairo-Dock related
to Xfce.

%package	kde
Summary:	Plug-ins files for Cairo-Dock related to KDE
Requires:	cairo-dock-core%{?_isa} >= %{core_least_ver}
Requires:	%{name}-common = %{version}-%{release}

%description	kde
This package contains plug-ins files for Cairo-Dock related
to KDE.

%package	webkit
Summary:	Plug-ins files for Cairo-Dock related to WebKit
Requires:	cairo-dock-core%{?_isa} >= %{core_least_ver}
Requires:	%{name}-common = %{version}-%{release}

%description	webkit
This package contains plug-ins files for Cairo-Dock related
to WebKit.

%package	unstable
Summary:	Unstable plug-ins not installed by default
Requires:	cairo-dock-core%{?_isa} >= %{core_least_ver}
Requires:	%{name}-common = %{version}-%{release}

%description	unstable
This package contains unstable and experimental
plug-ins not installed by default.

%package	-n cairo-dock-python3
Summary:	Python3 binding for Cairo-Dock
Requires:	cairo-dock-core >= %{core_least_ver}
Requires:	%{name}-dbus = %{version}-%{release}
Requires:	python3-gobject
Requires:	python3-dbus
Obsoletes:	cairo-dock-python3 < 3.5.99^20241007git019f49f-1

%description	-n cairo-dock-python3
This package contains Python3 binding files for Cairo-Dock

%package	-n cairo-dock-ruby
Summary:	Ruby binding for Cairo-Dock
Requires:	cairo-dock-core >= %{core_least_ver}
Requires:	%{name}-common = %{version}-%{release}
Requires:	ruby(release)
Requires:	rubygem(ruby-dbus)
Requires:	rubygem(parseconfig)
BuildArch:	noarch

%description	-n cairo-dock-ruby
This package contains Ruby binding files for Cairo-Dock

%package	-n cairo-dock-vala
Summary:	Vala binding for Cairo-Dock
Requires:	cairo-dock-core%{?_isa} >= %{core_least_ver}
Requires:	%{name}-common = %{version}-%{release}
Requires:	vala

%description	-n cairo-dock-vala
This package contains Vala binding files for Cairo-Dock

%package	-n cairo-dock-vala-devel
Summary:	Development files for Vala binding for Cairo-Dock
Requires:	cairo-dock-vala%{?_isa} = %{version}-%{release}
Requires:	%{name}-dbus%{?isa} = %{version}-%{release}

%description	-n cairo-dock-vala-devel
This package contains development files for Vala
binding for Cairo-Dock.

%prep
%setup -q -n cairo-dock-plugins-%{mainver}%{?use_git:-%{gitdate}git%{shorthash}}
%patch -P11 -p1 -b .wk2
%patch -P13 -p1 -b .wk2_gtk41

## permission
# %%_fixperms cannot fix permissions completely here
for dir in */
do
	find $dir -type f | xargs -r chmod 0644
done
chmod 0644 [A-Z]* copyright
chmod 0755 */

# cmake issue
sed -i.debuglevel \
	-e '\@add_definitions@s|-O3|-O2|' \
	CMakeLists.txt
sed -i.stat \
	-e 's|\${MSGFMT_EXECUTABLE}|\${MSGFMT_EXECUTABLE} --statistics|' \
	po/CMakeLists.txt

# Compilation flags
sed -i.wall \
	-e 's|-Wno-all||' \
	Dbus/interfaces/vala/src/CMakeLists.txt

## source code fix
## Bindings
# Ruby
sed -i.site \
	-e "s|CONFIG\['rubylibdir'\]|CONFIG['vendorlibdir']|" \
	CMakeLists.txt
# ????
sed -i.installdir \
	-e '\@REGEX REPLACE.*RUBY@d' \
	-e '\@set.*RUBY_LIB_DIR.*CMAKE_INSTALL_PREFIX.*RUBY_LIB_DIR_INSTALL@d' \
	CMakeLists.txt

# Modify version forcely
sed -i CMakeLists.txt -e '\@set (\(CORE_REQUIRED_\|\)VERSION @s|VERSION.*|VERSION "%{mainver}")|'

# Kill python2 explicitly
sed -i.py2 CMakeLists.txt -e 's|python2)|python2-nono)|'
# ... and explicitly use python3
env LANG=C grep -rl /usr/bin/env . | \
	xargs sed -i -e 's|/usr/bin/env[ \t]*python$|/usr/bin/python3|'

%build
%set_build_flags

%if 0%{?use_gcc_strict_sanitize}
export CC="${CC} -fsanitize=address -fsanitize=undefined"
export CXX="${CXX} -fsanitize=address -fsanitize=undefined"
export LDFLAGS="${LDFLAGS} -pthread"
%endif

rm -f CMakeCache.txt
%cmake -B. \
%if 0%{?build_unstable} >= 1
	-Denable-disks=TRUE \
	-Denable-doncky=TRUE \
	-Denable-global-menu=TRUE \
	-Denable-network-monitor=TRUE \
%if 0
	-Denable-scooby-do=TRUE \
%endif
%endif
	.

%make_build

%install
%make_install \
	INSTALL="install -p"

# Collect documents
rm -rf documents licenses documents-dbus
mkdir documents licenses documents-dbus
cp -a \
	ChangeLog \
	documents
mkdir documents-dbus/Dbus
cp -a Dbus/demos \
	documents-dbus/Dbus/
cp -a \
	LGPL-2 \
	LICENSE \
	copyright \
	licenses/

# Just to suppress rpmlint...
pushd $RPM_BUILD_ROOT

for f in \
	`find . -name \*.conf`
do
	sed -i -e '1i\ ' $f
done

set +x
for f in \
	.%{_datadir}/cairo-dock/plug-ins/*/* \
	$(find . -name \*.rb)
do
	if head -n 1 $f 2>/dev/null | grep -q /bin/ ; then 
		set -x
		chmod 0755 $f
		set +x
	fi
done

# Modify CDApplet.h not to contain %%buildroot strings
sed -i .%{_datadir}/cairo-dock/plug-ins/Dbus/CDApplet.h \
	-e '\@def@s|__.*\(DBUS_INTERFACES_VALA_SRC_CDAPPLET_H__\)|__\1|'

popd

%find_lang cairo-dock-plugins

%ldconfig_scriptlets -n cairo-dock-vala

%files	common
%license	licenses/*

%files
# This is a metapackage

%files	base -f cairo-dock-plugins.lang
%doc	documents/*

%{_libdir}/cairo-dock/*
%{_datadir}/cairo-dock/plug-ins/*
%{_datadir}/cairo-dock/gauges/*/

%exclude	%{_libdir}/cairo-dock/*weblet*
%exclude	%{_libdir}/cairo-dock/*xfce*
%exclude	%{_libdir}/cairo-dock/*kde*
%exclude	%{_libdir}/cairo-dock/*Dbus*
%exclude	%{_datadir}/cairo-dock/plug-ins/*weblet*
%exclude	%{_datadir}/cairo-dock/plug-ins/*xfce*
%exclude	%{_datadir}/cairo-dock/plug-ins/*kde*
%exclude	%{_datadir}/cairo-dock/plug-ins/Dbus/
%if 0%{?build_unstable} >= 1
%exclude	%{_libdir}/cairo-dock/appmenu-registrar
%exclude	%{_libdir}/cairo-dock/libcd-Global-Menu.so
%exclude	%{_libdir}/cairo-dock/libcd-disks.so
%exclude	%{_libdir}/cairo-dock/libcd-doncky.so
%exclude	%{_libdir}/cairo-dock/libcd-network-monitor.so
#%%exclude	%%{_libdir}/cairo-dock/libcd-scooby-do.so
%exclude	%{_datadir}/cairo-dock/plug-ins/Disks/
%exclude	%{_datadir}/cairo-dock/plug-ins/Doncky/
%exclude	%{_datadir}/cairo-dock/plug-ins/Global-Menu/
%exclude	%{_datadir}/cairo-dock/plug-ins/Network-Monitor/
#%%exclude	%%{_datadir}/cairo-dock/plug-ins/Scooby-Do/
%endif
# Vala
%exclude	%{_datadir}/cairo-dock/plug-ins/Dbus/CDApplet.h

%if 0%{?build_unstable} >= 1
%files	unstable
%{_libdir}/cairo-dock/appmenu-registrar
%{_libdir}/cairo-dock/libcd-Global-Menu.so
%{_libdir}/cairo-dock/libcd-disks.so
%{_libdir}/cairo-dock/libcd-doncky.so
%{_libdir}/cairo-dock/libcd-network-monitor.so
#%%{_libdir}/cairo-dock/libcd-scooby-do.so
%{_datadir}/cairo-dock/plug-ins/Disks/
%{_datadir}/cairo-dock/plug-ins/Doncky/
%{_datadir}/cairo-dock/plug-ins/Global-Menu/
%{_datadir}/cairo-dock/plug-ins/Network-Monitor/
#%%{_datadir}/cairo-dock/plug-ins/Scooby-Do/
%endif

%files	dbus
%doc	documents-dbus/*
%{_libdir}/cairo-dock/*Dbus*
%{_datadir}/cairo-dock/plug-ins/Dbus/
# The following is for cairo-dock-vala-devel
%exclude	%{_datadir}/cairo-dock/plug-ins/Dbus/CDApplet.h

%files	xfce
%{_libdir}/cairo-dock/*xfce*
%{_datadir}/cairo-dock/plug-ins/*xfce*

%files	kde
%{_libdir}/cairo-dock/*kde*
%{_datadir}/cairo-dock/plug-ins/*kde*

%files	webkit
%{_libdir}/cairo-dock/*weblet*
%{_datadir}/cairo-dock/plug-ins/*weblet*

%files	-n cairo-dock-python3
%{python3_sitearch}/CairoDock.py*
%{python3_sitearch}/CDApplet.py*
%{python3_sitearch}/CDBashApplet.py*
%{python3_sitearch}/__pycache__/

%files	-n cairo-dock-ruby
%{ruby_vendorlib}/CDApplet.rb

%files -n cairo-dock-vala
%{_libdir}/libCDApplet.so.1*
%{_datadir}/vala/vapi/CDApplet.*

%files -n cairo-dock-vala-devel
%{_libdir}/libCDApplet.so
%{_libdir}/pkgconfig/CDApplet.pc
%{_datadir}/cairo-dock/plug-ins/Dbus/CDApplet.h

%changelog
* Fri Feb 14 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.99^20250214git2fabf99-1.rc2
- Update to the latest git (20250214git2fabf99)

* Thu Feb 13 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.99^20250211git4793755-1.rc1
- Update to the latest git (20250211git4793755)

* Thu Jan 30 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.99^20250120git9cc48a3-1.rc1
- Update to the latest git (20250120git9cc48a3)

* Sun Jan 19 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.99^20250118git18ad738-1.beta7
- Update to the latest git (20250118git18ad738)

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.99^20241217gitf8ad97e-2.beta6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 17 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.99^20241217gitf8ad97e-1.beta6
- Update to the latest git (20241217gitf8ad97e)

* Mon Dec 16 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.99^20241216gitce0764f-1.beta6
- Update to the latest git (20241216gitce0764f)

* Sun Dec 08 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.99^20241207gitce518e9-1
- Update to the latest git (20241207gitce518e9)

* Tue Nov 19 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.99^20241117gite9d3fcd-1
- Update to the latest git (3.5.99-20241117gite9d3fcd)

* Thu Oct 24 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.99^20241024gitd965212-1
- Update to the latest git (20241024gitd965212)

* Sun Oct 06 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.99^20241007git019f49f-1
- Update to the latest git (20241007git019f49f)

* Sun Sep 22 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.99^20240501git9901f7d-5
- BR: ayatana-indicator3-0.4 for Messaging-Menu support

* Fri Aug 16 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.99^20240501git9901f7d-4
- Require gdk-pixbuf2-modules-extra if available

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.99^20240501git9901f7d-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.5.99^20240501git9901f7d-2
- Rebuilt for Python 3.13

* Sat May 04 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.99^20240501git9901f7d-1
- Update to the latest git (20240501git9901f7d)

* Wed Mar 27 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.0-4
- Fix invalid SPDX tag

* Fri Mar 15 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.0-3
- SPDX migration

* Fri Mar 08 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.0-2
- vala: regenerate C source from vala source properly
  and reenable -Werror=incompatible-pointer-types

* Mon Feb 26 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.0-1
- Update to 3.5.0

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-49.20210730gitf24f769
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-48.20210730gitf24f769
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-47.20210730gitf24f769
- Change -Wincompatible-pointer-types from error to warning

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-46.20210730gitf24f769
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 3.4.1-45.20210730gitf24f769
- Rebuilt for Python 3.12

* Mon May 29 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-44.20210730gitf24f769
- Pass -r option to xargs because new rpm creates empty directory

* Sun May 07 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-43.20210730gitf24f769
- Use webkit2gtk-4.1 for F-39+
  https://fedoraproject.org/wiki/Changes/Remove_webkit2gtk-4.0_API_Version

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-42.20210730gitf24f769.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan  3 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-42.20210730gitf24f769
- Handle PEP632, switch from distutils to setuptools

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-41.20210730gitf24f769.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.4.1-41.20210730gitf24f769.3
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-41.20210730gitf24f769.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 3.4.1-41.20210730gitf24f769.1
- Rebuilt with OpenSSL 3.0.0

* Tue Aug 10 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-41.20210730gitf24f769
- Update to the latest git

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-40.20210125gitcad0a29.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.4.1-40.20210125gitcad0a29.1
- Rebuilt for Python 3.10

* Sat Jan 30 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-40.20210125gitcad0a29
- Update to the latest git

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-39.20210103git8554994.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan  7 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-39.20210103git8554994
- Update to the latest git

* Sun Jan  3 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-38.20201022gita0d3415
- Update to the latest git

* Fri Aug  7 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-37
- Minor fix for cmake build issue https://fedoraproject.org/wiki/Changes/CMake_to_do_out-of-source_builds

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-37
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.4.1-35
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-33
- Fix for gcc10 -fno-common

* Thu Nov 28 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-32
- Use newer zeitgeist

* Thu Nov 28 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-31
- Quick-and-dirty workaround for libetpan 1.9.4 change using pkgconfig

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.4.1-30
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Aug 20 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-29
- F-31+: disable python2 binding, use python3 explicitly

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.4.1-27
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 3.4.1-25
- Require python2/python3-gobject instead of pygobject2 and pygobject3

* Fri Feb  1 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-24
- Fix for recent cmake change

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.4.1-22
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-20
- Remove -z defs for plugins usage

* Fri Dec 15 2017 Iryna Shcherbina <ishcherb@redhat.com> - 3.4.1-19
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Nov 22 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-18
- F-28: use vte-2.91 instead of vte-2.90

* Tue Nov 14 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-17
- F-28: rebuild for new libical

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr  1 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-14
- Fix FTBFS with related to -Wno-all -Werror=format-security
- F-26+: switch to use webkitgtk4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.4.1-12
- Rebuild for Python 3.6

* Sun Dec 11 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-11
- Workaround for time.h related conflict with 2.25 glibc

* Sat Dec 10 2016 Andreas Bierfert <andreas.bierfert@lowlatency.de> - 3.4.1-10
- rebuild for libetpan 1.7.2 soname change
- fix changelog dates

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 24 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-8
- Pull in upstream patch to update URL on weather plugin

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 David Tardon <dtardon@redhat.com> - 3.4.1-6
- rebuild for libical 2.0.0

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 25 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-3
- Require xdg-utils by default for logout

* Wed Mar 25 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-2
- Default to xdg-screensaver for lock_screen
- Restrict the dependency for core package

* Fri Mar 13 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-1
- 3.4.1
- demo_ruby: fix traceback when changing themes

* Sat Feb 28 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.0-14
- Bump release

* Wed Feb 25 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.0-13
- Cosmetic changes

* Wed Feb 11 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.0-12
- Split out Dbus subpackage, modify internal dependency
- Make some packages noarch

* Fri Jan 23 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.0-11
- Another may-be-problematic contents removed (bug 1178912)
- Make sure that licenses files are always installed

* Thu Jan 22 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.0-10
- Some may-be-problematic contents removed (bug 1178912)

* Fri Jan 02 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.0-9
- Initial package
