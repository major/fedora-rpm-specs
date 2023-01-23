%if 0%{?fedora} >= 20 && 0%{?rhel} > 7
%bcond_with wayland
%else
%bcond_without wayland
%endif

Name:          waffle
Version:       1.6.1
Release:       7%{?dist}
Summary:       Platform independent GL API layer

License:       MIT
URL:           http://www.waffle-gl.org/releases.html
Source0:       https://gitlab.freedesktop.org/mesa/waffle/-/raw/website/files/release/waffle-%{version}/waffle-%{version}.tar.xz

BuildRequires: cmake libxslt docbook-style-xsl libxcb-devel
BuildRequires: gcc-c++
BuildRequires: libX11-devel mesa-libGL-devel mesa-libGLU-devel
BuildRequires: chrpath
BuildRequires: mesa-libEGL-devel
%if 0%{?rhel} > 6 || 0%{?fedora} > 0
BuildRequires: mesa-libGLES-devel
BuildRequires: systemd-devel
%endif
BuildRequires: mesa-libgbm-devel
%if %{with wayland}
BuildRequires: wayland-devel
%endif

%description
Waffle is a cross-platform C library that allows one to defer
selection of GL API and of window system until runtime.


%package devel
Summary:    Development headers and libraries for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
Contains the header files, and libraries required for development of
%{name}-related software.

%package doc
Summary:    Documentation for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description doc
Contains HTML version of the developer documentation for development of
%{name}-related software (manpages are in the -devel package).


%package examples
Summary:    Example programs using %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description examples
Example programs using %{name}.


%prep
%setup -q


%build
%cmake \
    -DCMAKE_INSTALL_DOCDIR:PATH=%{_defaultdocdir}/%{name}-%{version} \
    -DCMAKE_BUILD_STRIP=FALSE \
    -Dwaffle_has_glx=1 -Dwaffle_has_gbm=1 \
%if %{with wayland}
    -Dwaffle_has_wayland=1 \
%endif
    -Dwaffle_build_manpages=1 -Dwaffle_build_htmldocs=1

%cmake_build

# We don’t want to install binary files in %%docdir
rm -rf examples/CMakeFiles

%install
%cmake_install
# Fedora now uses unversioned doc dirs, make install shouldn’t try to
# install there anyway.
rm -rf %{buildroot}%{_docdir}/%{name}*

%ldconfig_scriptlets


%files
%license LICENSE.txt
%doc README.md
%{_libdir}/lib%{name}*.so.*
%{_bindir}/wflinfo
%{_datadir}/bash-completion/completions/wflinfo

%files doc
%doc doc/html/

%files devel
%doc doc/release-notes/
%{_includedir}/waffle*
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/%{name}*
%{_libdir}/cmake/Waffle/*
%{_mandir}/man*/*


%files examples
%doc examples/


%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 01 2020 Kalev Lember <klember@redhat.com> - 1.6.1-1
- Update to 1.6.1
- Use license macro for LICENSE.txt

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Matěj Cepl <mcepl@redhat.com> - 1.5.2-8
- Add BuildRequires gcc per new PG.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 29 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.5.2-3
- Fix Wayland conditionals so it's enabled in Fedora

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 09 2015 Dave Airlie <airlied@redhat.com> 1.5.2-1
- 1.5.2 release

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 5 2015 Matěj Cepl <mcepl@redhat.com> - 1.5.0-3
- Make package building on RHEL-6.

* Mon Jan 05 2015 Matej Cepl <mcepl@redhat.com> - 1.5.0-2
- Package examples again.

* Tue Dec 16 2014 Dave Airlie <airlied@redhat.com> 1.5.0-1
- 1.5.0 release

* Thu Dec 04 2014 Matej Cepl <mcepl@redhat.com> - 1.4.2-2
- Merge with master.
- Patch out commit 92116dae to make building possible on cmake < 2.8.12.

* Thu Dec 04 2014 Matej Cepl <mcepl@redhat.com> - 1.4.2-1
- Upstream release (#1161826)

* Tue Sep 23 2014 Matěj Cepl <mcepl@redhat.com> - 1.4.0-1
- Upgreade to the latest upstream release (RHBZ# 1145481)

* Tue Sep 23 2014 Matej Cepl <mcepl@redhat.com> - 1.3.0-5
- Apply patch to make GBM work on f21 as well.

* Tue Sep 23 2014 Matěj Cepl <mcepl@redhat.com> - 1.3.0-4
- Enable GBM and Wayland options as well.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct 01 2013 Matěj Cepl <mcepl@redhat.com> - 1.3.0-1
- Upstream release.

* Fri Sep 27 2013 Matěj Cepl <mcepl@redhat.com> - 1.2.3-4
- And even more fixes (switch on man and HTML doc generation).

* Thu Sep 26 2013 Matěj Cepl <mcepl@redhat.com> - 1.2.3-3
- Fix even more errors indicated by the package review.

* Mon Aug 26 2013 Matěj Cepl <mcepl@redhat.com> - 1.2.3-2
- Fix errors indicated by the package review.

* Sat Aug 24 2013 Matěj Cepl <mcepl@redhat.com> - 1.2.3-1
- New upstream release.

* Thu Nov 15 2012 Matěj Cepl <mcepl@redhat.com> - 1.2.0-1
- Upstream upgrade.

* Fri Oct 19 2012 Matěj Cepl <mcepl@redhat.com> - 1.1.1-1
- First experimental build.
