Name:		globus-net-manager
%global _name %(tr - _ <<< %{name})
Version:	1.7
Release:	11%{?dist}
Summary:	Grid Community Toolkit - Network Manager Library

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15.27
BuildRequires:	globus-xio-devel >= 5
%if %{?fedora}%{!?fedora:0} >= 30 || %{?rhel}%{!?rhel:0} >= 8
BuildRequires:	python3-devel
%else
BuildRequires:	python2-devel
%endif
BuildRequires:	doxygen
BuildRequires:	perl-interpreter
BuildRequires:	perl(strict)

Requires:	globus-common%{?_isa} >= 15.27

%package devel
Summary:	Grid Community Toolkit - Network Manager Library Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package -n globus-xio-net-manager-driver
Summary:	Grid Community Toolkit - Globus XIO Network Manager Driver
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	globus-xio%{?_isa} >= 5

%package -n globus-xio-net-manager-driver-devel
Summary:	Grid Community Toolkit - Globus XIO Network Manager Driver Development Files
Requires:	globus-xio-net-manager-driver%{?_isa} = %{version}-%{release}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%package doc
Summary:	Grid Community Toolkit - Network Manager Library Documentation Files
BuildArch:	noarch

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Network Manager Library

The Globus Neteork Manager Library is a plug-in point for network management
tasks, such as:
 - selectively open ports in a firewall and allow these ports to be closed
   when transfers are complete
 - configure a virtual circuit based on a site policy and route traffic
   over this circuit
 - route network traffic related to a task over a particular network

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
Network Manager Library Development Files

%description -n globus-xio-net-manager-driver
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The globus-xio-net-manager-driver package contains:
Globus XIO Network Manager Driver

%description -n globus-xio-net-manager-driver-devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The globus-xio-net-manager-driver-devel package contains:
Globus XIO Network Manager Driver Development Files

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
Network Manager Library Documentation Files

%prep
%setup -q -n %{_name}-%{version}

%build
# Reduce overlinking
export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"

%if %{?fedora}%{!?fedora:0} >= 30 || %{?rhel}%{!?rhel:0} >= 8
export PYTHON_CONFIG=%{__python3}-config
%else
export PYTHON_CONFIG=%{__python2}-config
%endif

%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir} \
	   --enable-python

# Reduce overlinking
sed 's!CC \(.*-shared\) !CC \\\${wl}--as-needed \1 !' -i libtool

%make_build

%install
%make_install

# Remove libtool archives (.la files)
rm %{buildroot}%{_libdir}/*.la

# Install README file
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README

# Remove license file from pkgdocdir
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE

%check
GLOBUS_HOSTNAME=localhost PYTHONDONTWRITEBYTECODE=1 %make_build check

%ldconfig_scriptlets

%ldconfig_scriptlets -n globus-xio-net-manager-driver

%files
%{_libdir}/libglobus_net_manager.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files devel
%{_includedir}/globus/globus_net_manager.h
%{_includedir}/globus/globus_net_manager_attr.h
%{_libdir}/libglobus_net_manager.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n globus-xio-net-manager-driver
# This is a loadable module (plugin)
%{_libdir}/libglobus_xio_net_manager_driver.so

%files -n globus-xio-net-manager-driver-devel
%{_includedir}/globus/globus_xio_net_manager_driver.h
%{_libdir}/pkgconfig/globus-xio-net-manager-driver.pc

%files doc
%doc %{_mandir}/man3/*
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/html
%doc %{_pkgdocdir}/html/*
%license GLOBUS_LICENSE

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.7-9
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.7-5
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.7-2
- Rebuilt for Python 3.11

* Wed May 25 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.7-1
- New GCT release v6.2.20220524

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 17 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.6-1
- Doxygen fix

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.5-1
- Minor fixes to makefiles
- Add BuildRequires perl-interpreter
- Specfile updates

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.4-1
- Check python-config for --embed flag (python 3.8 compatibility)
- Drop patch globus-net-manager-python-embed.patch

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-4
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 12 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.3-2
- Check python-config for --embed flag (python 3.8 compatibility)

* Tue Feb 26 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.3-1
- Doxygen fixes (1.2)
- Python 3 support (1.3)
- Build using Python 3 for Fedora 30+
- Enable checks

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.1-1
- Switch upstream to Grid Community Toolkit
- First Grid Community Toolkit release (1.0)
- Merge GT6 update 0.18 into GCT (1.1)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 03 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.18-1
- GT6 update: Fix pre-connect not using changed remote contact

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.17-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.17-1
- GT6 update: Fix .pc typo
- Drop patch globus-net-manager-pkgconfig.patch (fixed upstream)

* Mon Mar 27 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.16-3
- EPEL 5 End-Of-Life specfile clean-up
  - Remove Group and BuildRoot tags
  - Remove _pkgdocdir macro definition
  - Drop redundant Requires corresponding to autogenerated pkgconfig Requires
  - Don't clear the buildroot in the install section
  - Remove the clean section
- Fix misspelled dependency in pkgconfig file

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 04 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.16-1
- GT 6 update: Exclude tests from doc

* Mon May 02 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.15-1
- GT6 update

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.14-1
- GT6 update (pre_connect return attrs get set on attr, not handle)

* Tue Nov 24 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.13-1
- GT6 update (Remove unused code)

* Mon Jul 27 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.12-1
- GT6 update (Fix memory leaks, NULL pointer derefs, and dead assignments)

* Sun Jul 12 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.10-1
- GT6 update (Fix uninitialized value, Remove unused variables)

* Sat Jun 20 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.9-1
- GT6 update (cleanups)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 15 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.8-1
- GT6 update (fix for attr not being used on connect)

* Mon Mar 30 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.7-1
- GT6 update (add file parameter to logging driver to set a file to log to)

* Fri Jan 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.6-2
- Implement updated license packaging guidelines

* Thu Jan 15 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.6-1
- GT6 update (test enhancements)
- Extend package description

* Thu Jan 08 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.2-1
- Initial packaging
