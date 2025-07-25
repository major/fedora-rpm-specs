# Use lower fortification level
# https://github.com/stevengj/nlopt/issues/563
%global _fortify_level 2

# Prevent accidental soname bumps.
%global sover        1

# Conditionals controlling the build.
%global with_guile   1
%global with_octave  1
%global with_py3     1

# Guile version
%if 0%{?fedora}
%global guile_ver    3.0
%endif
%global guile_pkg    %(echo guile%{?guile_ver} | sed -e 's!\\\.!!g')

%global relversion 2.10.0
Name:              NLopt
Version:           2.10.0
%global tag        v%{version}
Release:           3%{?dist}
Summary:           Open-Source library for nonlinear optimization

# Get a lowercase name for virtual provides.
%global lc_name    %{lua:print(string.lower(rpm.expand("%{name}")))}

# The detailed license-breakdown of the sources is:
#
# BSD (2 clause)
# --------------
# util/mt19937ar.c
#
#
# BSD (3 clause)
# --------------
# slsqp/*
#
#
# LGPL (v2 or later)
# ------------------
# luksan/*
#
# MIT/X11 (BSD like)
# ------------------
# api/*    auglag/*  bobyqa/*      cdirect/*  cobyla/*
# cquad/*  crs/*     direct/*      esch/*     isres/*
# mlsl/*   mma/*     neldermead/*  newuoa/*   octave/*
# stogo/*  tensor/*  test/*        util/* (ex. util/mt19937ar.c)
#
#
# Public Domain
# -------------
# praxis/*  subplex/*
#
# Automatically converted from old format: BSD and LGPLv2+ and MIT and Public Domain - review is highly recommended.
License:           LicenseRef-Callaway-BSD AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-Public-Domain
URL:               http://ab-initio.mit.edu/%{lc_name}
Source0:           https://github.com/stevengj/%{lc_name}/archive/%{tag}/%{lc_name}-%{version}.tar.gz

# Kill RPATH.
Patch0:            nlopt-2.9.1-kill_rpath.patch

BuildRequires:     cmake3
BuildRequires:     gcc
BuildRequires:     gcc-c++
BuildRequires:     gcc-gfortran
BuildRequires:     make
BuildRequires:     ncurses-devel

# The "gnulib" is a copylib and has a wildcard-permission from FPC.
# See: https://fedorahosted.org/fpc/ticket/174
Provides:          bundled(gnulib)
Provides:          %{lc_name}                                      =  %{version}-%{release}
Provides:          %{lc_name}%{?_isa}                              =  %{version}-%{release}

%description
NLopt is a library for nonlinear local and global optimization, for
functions with and without gradient information.  It is designed as
as simple, unified interface and packaging of several free/open-source
nonlinear optimization libraries.

It features bindings for GNU Guile, Octave and Python.  This build has
been made with C++-support enabled.


%package devel
Summary:           Development files for %{name}

Requires:          %{name}%{?_isa}                                 =  %{version}-%{release}
Provides:          %{lc_name}-devel                                =  %{version}-%{release}
Provides:          %{lc_name}-devel%{?_isa}                        =  %{version}-%{release}

%description devel
This package contains development files for %{name}.


%package doc
Summary:           Documentation files for %{name}
BuildArch:         noarch
Provides:          %{lc_name}-doc                                  =  %{version}-%{release}

%description doc
This package contains documentation files for %{name}.


%if 0%{?with_guile}
%package -n guile-%{name}
%{!?guile_pkgconf: %global guile_pkgconf %(%___build_pre; pkg-config --list-all | grep guile%{?guile_ver:-%{guile_ver}} | sed -e 's! .*$!!g')}
%{!?guile_sitedir: %global guile_sitedir %(%___build_pre; pkg-config --variable=sitedir %{guile_pkgconf})}
%{!?guile_extdir:  %global guile_extdir  %(%___build_pre; pkg-config --variable=extensiondir %{guile_pkgconf})}

Summary:           Guile bindings for %{name}

BuildRequires:     %{guile_pkg}-devel
BuildRequires:     pkgconfig
BuildRequires:     swig

Requires:          %{guile_pkg}%{?_isa}
Requires:          %{name}%{?_isa}                                 =  %{version}-%{release}

Provides:          guile-%{lc_name}                                =  %{version}-%{release}
Provides:          guile-%{lc_name}%{?_isa}                        =  %{version}-%{release}

%description -n guile-%{name}
This package contains Guile bindings for %{name}.
%endif


%if 0%{?with_octave}
%package -n octave-%{name}
%global octpkg %{name}
Summary:           Octave bindings for %{name}

BuildRequires:     octave-devel

Requires:          %{name}%{?_isa}                                 =  %{version}-%{release}
Requires:          octave
Requires(post):    octave
Requires(postun):  octave

Provides:          octave-%{lc_name}                               =  %{version}-%{release}
Provides:          octave-%{lc_name}%{?_isa}                       =  %{version}-%{release}

%description -n octave-%{name}
This package contains the Octave bindings for %{name}.
%endif


%if 0%{?with_py3}
%package -n python%{python3_pkgversion}-%{name}
Summary:           Python3 bindings for %{name}

BuildRequires:     python%{python3_pkgversion}-devel
BuildRequires:     python%{python3_pkgversion}-numpy

Requires:          %{name}%{?_isa}                                 =  %{version}-%{release}

Provides:          python%{python3_pkgversion}-%{lc_name}          =  %{version}-%{release}
Provides:          python%{python3_pkgversion}-%{lc_name}%{?_isa}  =  %{version}-%{release}

%description -n python%{python3_pkgversion}-%{name}
This package contains Python3 bindings for %{name}.
%endif


%prep
%autosetup -n %{lc_name}-%{version} -p 1

# Move all %%doc to topdir and append their belonging.
[[ -f README.md ]] &&  \
mv -f README.md README
_topdir="`pwd`"
for _dir in `find . -type d |                              \
  sed -e "/\.libs/d" -e "s/\.\///g" -e "/\./d" | sort -u`
do
  pushd ${_dir}
  for _file in 'AUTHOR*' 'COPY*' 'README*' '*[Pp][Dd][Ff]'
  do
    for _doc in `find . -maxdepth 1 -name "${_file}"`
    do
      mv -f ${_doc} ${_topdir}/${_doc}.`echo ${_dir} | sed -e "s/\//_/g"`
    done
  done
  popd
done


%build
%cmake3                                     \
  -DNLOPT_CXX=ON                            \
  -DNLOPT_FORTRAN=ON                        \
  -DNLOPT_PYTHON=ON                         \
  -DNLOPT_OCTAVE=ON                         \
  -DNLOPT_MATLAB=OFF                        \
  -DNLOPT_GUILE=ON                          \
  -DNLOPT_SWIG=ON                           \
  -DNLOPT_TESTS=ON                          \
  -DBUILD_SHARED_LIBS=ON                    \
  -DPYTHON_EXECUTABLE=%{__python3}          \
  -DINSTALL_PYTHON_DIR=%{python3_sitearch}  \
  -DINSTALL_M_DIR=%{octpkgdir}              \
  -DINSTALL_OCT_DIR=%{octpkglibdir}
%cmake3_build


%install
%cmake3_install

# We don't want these static-libs and libtool-dumplings
find %{buildroot} -depth -name '*.*a' -print0 | xargs -0 rm -f

%if 0%{?with_octave}
# Setup octave stuff properly.
mkdir -p %{buildroot}%{octpkgdir}/packinfo
chmod 0755 %{buildroot}%{octpkglibdir}/*.oct
install -pm 0644 COPYING %{buildroot}%{octpkgdir}/packinfo

cat > %{buildroot}%{octpkgdir}/packinfo/DESCRIPTION << EOF
Name: %{name}
Version: %{version}
Date: %(date +%Y-%m-%d)
Author: Steven G. Johnson <stevenj@alum.mit.edu>
Title: Open-Source library for nonlinear optimization
Description: NLopt is a library for nonlinear local and global
 optimization, for functions with and without gradient information.
 It is designed as as simple, unified interface and packaging of
 several free/open-source nonlinear optimization libraries.
Url: %{url}
EOF

cat > %{buildroot}%{octpkgdir}/packinfo/on_uninstall.m << EOF
function on_uninstall (desc)
  error ('Can not uninstall %s installed by the redhat package manager', desc.name);
endfunction
EOF
%endif


%check
%ctest3


%ldconfig_scriptlets


%if 0%{?with_octave}
%post -n octave-%{name}
%octave_cmd pkg rebuild


%preun -n octave-%{name}
%octave_pkg_preun


%postun -n octave-%{name}
%octave_cmd pkg rebuild
%endif


%files
%doc ChangeLog NEWS.md
%license COPY*
%{_libdir}/lib%{lc_name}.so.%{sover}*


%files devel
%doc %{_mandir}/man3/*
%{_includedir}/*
%{_libdir}/cmake/nlopt/
%{_libdir}/lib%{lc_name}.so
%{_libdir}/pkgconfig/%{lc_name}.pc


%files doc
%doc AUTHOR* ChangeLog NEWS.md README* TODO *.[Pp][Dd][Ff].*
%license COPY*


%if 0%{?with_guile}
%files -n guile-%{name}
%{guile_extdir}/*nlopt_guile.so
%{guile_sitedir}/*
%endif


%if 0%{?with_octave}
%files -n octave-%{name}
%{octpkglibdir}
%{octpkgdir}
%endif


%files -n python%{python3_pkgversion}-%{name}
%{python3_sitearch}/*.so*
%{python3_sitearch}/*.py*
%{python3_sitearch}/__pycache__/*.py*
%dir %{python3_sitearch}/%{lc_name}-%{relversion}.dist-info
%{python3_sitearch}/%{lc_name}-%{relversion}.dist-info/METADATA

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 2.10.0-2
- Rebuilt for Python 3.14

* Thu Feb 06 2025 Björn Esser <besser82@fedoraproject.org> - 2.10.0-1
- Update to latest release 2.10.0
  Fixes: rhbz#2343834

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 27 2024 Benson Muite <benson_muite@emailplus.org> - 2.9.1-1
- Update to latest release 2.9.1

* Thu Nov 14 2024 Orion Poplawski <orion@nwra.com> - 2.8.0^202409167cdebfe-2
- Rebuild for octave 9.2

* Sun Sep 29 2024 Benson Muite <benson_muite@emailplus.org> - 2.8.0^202409167cdebfe-1
- Update to latest release
- Update to Guile 3.0 for Guile subpackage

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.7.1-21
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2.7.1-19
- Rebuilt for Python 3.13

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.7.1-15
- Rebuilt for Python 3.12

* Sat Jun 10 2023 Björn Esser <besser82@fedoraproject.org> - 2.7.1-14
- Fix build with CMake 3.27.0

* Sat Apr 08 2023 Orion Poplawski <orion@nwra.com> - 2.7.1-13
- Rebuild with octave 8.1.0

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.7.1-10
- Rebuilt for Python 3.11

* Wed Jun 01 2022 Orion Poplawski <orion@nwra.com> - 2.7.1-9
- Rebuild for octave 7.1

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Björn Esser <besser82@fedoraproject.org> - 2.7.1-7
- Also use ctest3 in %%check

* Tue Dec 14 2021 Björn Esser <besser82@fedoraproject.org> - 2.7.1-6
- Use cmake3 for build

* Tue Dec 14 2021 Björn Esser <besser82@fedoraproject.org> - 2.7.1-5
- Use unversioned system-provided guile for non-Fedora builds

* Thu Dec 09 2021 Kalev Lember <klember@redhat.com> - 2.7.1-4
- Backport upstream PR to fix guile detection in Fedora

* Sun Dec 05 2021 Björn Esser <besser82@fedoraproject.org> - 2.7.1-3
- Build against guile22
  Fixes rhbz#2008436

* Sun Dec 05 2021 Björn Esser <besser82@fedoraproject.org> - 2.7.1-2
- Explicitly set configuration options
- Enable Fortran code
- Drop "-fpermissive" compiler flag

* Sat Dec 04 2021 Björn Esser <besser82@fedoraproject.org> - 2.7.1-1
- Update to 2.7.1
  Fixes rhbz#1899511

* Wed Aug 11 2021 Orion Poplawski <orion@nwra.com> - 2.6.2-11
- Rebuild for octave 6.3.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Björn Esser <besser82@fedoraproject.org> - 2.6.2-9
- Use out-of-tree-build cmake macros
- More spec file modernizations

* Mon Jun 21 2021 Björn Esser <besser82@fedoraproject.org> - 2.6.2-8
- Fix build by kiling RPATH (#1967199)
- Some spec file modernizations

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.6.2-7
- Rebuilt for Python 3.10

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 01 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.6.2-5
- Make the package build with updated %%cmake macro (#1863081)

* Thu Aug 20 2020 Jan Beran <jaberan@redhat.com> - 2.6.2-4
- Fix flatpak build

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 31 2020 Björn Esser <besser82@fedoraproject.org> - 2.6.2-1
- Update to 2.6.2

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-7
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Orion Poplawski <orion@nwra.com> - 2.6.1-5
- Rebuild with octave 64bit indexes

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Orion Poplawski <orion@cora.nwra.com> - 2.6.1-1
- Update to 2.6.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Orion Poplawski <orion@cora.nwra.com> - 2.5.0-1
- Update to 2.5.0, uses cmake
- Rebuild for octave 4.4

* Mon Sep 17 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.2-18
- Remove Python 2 subpackage on Fedora 30+ (#1627303)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.2-16
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.4.2-14
- Python 2 binary package renamed to python2-nlopt
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.4.2-10
- Rebuild for Python 3.6

* Wed Dec 07 2016 Orion Poplawski <orion@cora.nwra.com> - 2.4.2-9
- Rebuild for octave 4.2

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Jul 07 2015 Orion Poplawski <orion@cora.nwra.com> - 2.4.2-5
- Rebuild for octave 4.0
- Add patch for octave 4.0 support

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Björn Esser <bjoern.esser@gmail.com> - 2.4.2-2
- disable octave-subpkg on el7

* Thu Jul 17 2014 Björn Esser <bjoern.esser@gmail.com> - 2.4.2-1
- new upstream release (#1116586)
- adapted spec to use named conditionals for packages

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 2.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Jan 14 2014 Björn Esser <bjoern.esser@gmail.com> - 2.4.1-5
- fixed description-file for octave-NLopt (#1048510)

* Tue Jan 14 2014 Björn Esser <bjoern.esser@gmail.com> - 2.4.1-4
- fixed nlopt.pc to reflect the correct lib to link against

* Sat Dec 28 2013 Kevin Fenzi <kevin@scrye.com> - 2.4.1-3
- Rebuild to fix broken deps

* Sat Dec 28 2013 Björn Esser <bjoern.esser@gmail.com> - 2.4.1-2
- rebuild for octave-3.8.0-rc2

* Fri Dec 20 2013 Björn Esser <bjoern.esser@gmail.com> - 2.4.1-1
- new upstream release: v2.4.1
- adapted %%{source0} to match %%{name}
- changed `%%global lc_name` to `%%define lc_name`, because of globbing problems
- use `tr` instead of shell-builtin for `%%define lc_name`
- move `README.md` only if existing
- create an empty Makefile on el5 instead of modifying top-level Makefile.am
- do not autoreconf on el5
- append `-fpermissive` to C[XX]FLAGS on Fedora 19+

* Fri Dec 20 2013 Björn Esser <bjoern.esser@gmail.com> - 2.4-3.git20130903.35e6377
- made %%clean-target conditional on el5
- restructured spec-file for quick switching between snapshot and release
- moved package-specific macros to the corresponding subpackage

* Wed Oct 02 2013 Björn Esser <bjoern.esser@gmail.com> - 2.4-2.git20130903.35e6377
- adaptions for new Python-guidelines

* Thu Sep 19 2013 Björn Esser <bjoern.esser@gmail.com> - 2.4-1.git20130903.35e6377
- Initial rpm release (#1004209)
