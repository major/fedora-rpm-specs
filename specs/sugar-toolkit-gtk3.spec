%undefine _hardened_build

Name:    sugar-toolkit-gtk3
Version: 0.121
Release: 8%{?dist}
Summary: Sugar toolkit GTK+ 3
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     http://wiki.laptop.org/go/Sugar

Source0: http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.xz
Source1: macros.sugar
Patch0: Fix-logging-usage.patch

BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: gettext-devel
BuildRequires: gtk3-devel
BuildRequires: gobject-introspection-devel
BuildRequires: intltool
BuildRequires: librsvg2-devel
BuildRequires: libSM-devel
BuildRequires: perl-XML-Parser
BuildRequires: pkgconfig
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-gobject
# py-compile needs updating
BuildRequires: automake
Requires: python3-dateutil
Requires: python3-dbus
Requires: python3-gobject
Requires: python3-decorator
Requires: gettext-runtime
Requires: sugar-datastore
Requires: unzip
Requires: webkit2gtk4.1
Requires: git-core

%description
Sugar is the core of the OLPC Human Interface. The toolkit provides
a set of widgets to build HIG compliant applications and interfaces
to interact with system services like presence and the datastore.
This is the toolkit depending on GTK3.

%package devel
Summary: Invokation information for accessing SugarExt-1.0
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the invocation information for accessing
the SugarExt-1.0 library through gobject-introspection.

%prep
%autosetup -p1

%build
autoreconf
ls -1 %{_datadir}/automake-*/py-compile | sort | \
	tail -n 1 | while read f
do
	cp -p $f .
done

%configure
# There are missing dependencies in this project's Makefiles, in
# particular dependencies on libsugarext.   LTO is tripping these
# issues regularly.
make -O V=1 VERBOSE=1

%install
%make_install

mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d/
install -pm 644 %{SOURCE1} %{buildroot}/%{_rpmconfigdir}/macros.d/macros.sugar

%find_lang %name

#Remove libtool archives.
find %{buildroot} -type f -name "*.la" -delete

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%exclude %{_bindir}/sugar-activity
%{_bindir}/sugar-activity3
%{python3_sitelib}/*
%{_bindir}/sugar-activity-web
%{_rpmconfigdir}/macros.d/macros.sugar
%{_libdir}/girepository-1.0/*.typelib
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/*.so
%{_datadir}/gir-1.0/*.gir

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.121-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.121-7
- convert license to SPDX

* Thu Aug 15 2024 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 0.121-6
- Add git-core as a required dep

* Fri Aug 02 2024 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 0.121-5
- Fix logging usage

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.121-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Python Maint <python-maint@redhat.com> - 0.121-3
- Rebuilt for Python 3.13

* Tue May 07 2024 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 0.121-2
- Use gettext-rutime

* Tue Feb 06 2024 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 0.121-1
- New Release 0.121

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.120-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 27 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.120-6
- Update py-compile for python 3.12, imp module removed

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.120-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.120-4
- Rebuilt for Python 3.12

* Wed Apr 26 2023 Florian Weimer <fweimer@redhat.com> - 0.120-3
- Port to C99

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Oct 21 2022 Ibiam Chihurumnaya <ibiam@sugarlabs.org> 0.120-1
- New Release 0.120

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.119-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.119-2
- Rebuilt for Python 3.11

* Fri May 27 2022 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 0.119-1
- Change release

* Fri May 27 2022 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 0.119-1
- New release 0.119

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.118-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 16 2021 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 0.118-6
- Add Requires python3-decorator

* Fri Aug 06 2021 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 0.118-5
- Remove permission error patch

* Tue Aug 03 2021 Ibiam Chihurumnaya <ibiam@sugarlabs.org> - 0.118-4
- Apply permission error patch

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.118-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.118-2
- Rebuilt for Python 3.10

* Sun Feb 7 2021 Alex Perez <aperez@sugarlabs.org> - 0.116-10
- New release 0.118

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.116-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.116-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.116-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Jeff Law <law@redhat.org> - 0.116-10
- Disable parallel builds due to missing Makefile dependencies

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.116-10
- Rebuilt for Python 3.9

* Sun May 10 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.116-9
- Add patch to fix use of xml.etree.ElementTree

* Sat May 2 2020 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> 0.116-8
- Add upstream patch to fix sugar-install bundle

* Mon Mar 2 2020 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> 0.116-7
- Add upstream patch to build for python3 by default

* Sun Feb 2 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.116-6
- Add upstream patch to fix runtime error signal crash

* Sat Feb  1 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.116-5
- Re-add hardened disable

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.116-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.116-3
- Drop support for running legacy python2 activities

* Sat Jan 25 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.116-2
- Update for python3 builds

* Fri Jan 24 2020 Chihurumnaya Ibiam <ibiamchihurumnaya@gmail.com> 0.116-1
- Update to 0.116 release

* Wed Aug 28 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.114-1
- Update to 0.114 release

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.113-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 21 2019 Miro Hrončok <mhroncok@redhat.com> - 0.113-2
- Update Python requirements to be single version

* Tue Apr 16 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.113-1
- Update to sugar 0.113 release

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.112-6
- Minor cleanups

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.112-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Jan 12 2018 Tomas Popela <tpopela@redhat.com> - 0.112-2
- Adapt to the webkitgtk4 rename
