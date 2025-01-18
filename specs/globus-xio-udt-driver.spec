Name:		globus-xio-udt-driver
%global _name %(tr - _ <<< %{name})
Version:	2.3
Release:	9%{?dist}
Summary:	Grid Community Toolkit - Globus XIO UDT Driver

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-xio-devel >= 3
BuildRequires:	libnice-devel
BuildRequires:	udt-devel

%package devel
Summary:	Grid Community Toolkit - Globus XIO UDT Driver Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Globus XIO UDT Driver

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
Globus XIO UDT Driver Development Files

%prep
%setup -q -n %{_name}-%{version}

%build
# Reduce overlinking
export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"

%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir}

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

%ldconfig_scriptlets

%files
# This is a loadable module (plugin)
%{_libdir}/libglobus_xio_udt_driver.so
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files devel
%{_includedir}/globus/*
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 17 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.3-1
- Compatiility with libnice 0.1.18 (fixed upstream - drop patch)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.2-7
- Fix compilation with libnice 0.1.18

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.2-5
- Specfile updates

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.2-1
- Replace broken URL (2.1)
- Add AC_CONFIG_MACRO_DIR and ACLOCAL_AMFLAGS (2.2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.0-1
- Switch upstream to Grid Community Toolkit
- First Grid Community Toolkit release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 07 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.29-1
- GT6 update: Update gettext for win build

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 04 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.28-1
- GT6 update: Fix Glib build
- Drop patch globus-xio-udt-driver-glib.patch (accepted upstream)

* Thu Jun 22 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.27-1
- GT6 update: Don't force --static flag to pkg-config
- Drop some BuildRequires no longer needed with above change
- Fix undefined symbols during linking

* Mon Mar 27 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.25-3
- EPEL 5 End-Of-Life specfile clean-up
  - Remove Group and BuildRoot tags
  - Remove _pkgdocdir macro definition
  - Drop redundant Requires corresponding to autogenerated pkgconfig Requires
  - Don't clear the buildroot in the install section
  - Remove the clean section

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 04 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.25-1
- GT6 update

* Sat Sep 03 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.24-1
- GT6 update

* Sat Jun 04 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.23-1
- GT6 update: Allow building using the RHEL 6 version of libnice
- Drop patch globus-xio-udt-driver-oldnice.patch (accepted upstream)

* Fri May 27 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.21-1
- GT6 update: Add GLOBUS_XIO_UDT_STUNSERVER environment variable override

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.19-1
- GT6 update (Ignore other end's attempts at ipv6 negotiation)

* Mon Jul 27 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.18-2
- Update globus-xio-udt-driver-oldnice patch to build for EPEL 6 and 7

* Mon Jul 27 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.18-1
- GT6 update (Only allow IPv4 until udt driver supports IPv6)

* Sun Jul 12 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.17-1
- GT6 update (Fix error checking and implement GLOBUS_XIO_GET_STRING_OPTIONS)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.16-3
- Rebuilt for GCC 5 C++11 ABI change

* Thu Jan 22 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.16-2
- Implement updated license packaging guidelines
- Add missing Build-Requires (gupnp-igd-devel, libselinux-devel)

* Thu Nov 13 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.16-1
- GT6 update

* Fri Sep 12 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.15-1
- Initial packaging
