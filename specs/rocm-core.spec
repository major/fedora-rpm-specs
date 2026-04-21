#
# Copyright Fedora Project Authors.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
%global upstreamname rocm-core

%global pkg_library_name %{upstreamname}
%global pkg_library_version 1

%bcond_with preview
%if %{with preview}
%global rocm_release 7.12
%global rocm_patch 0
%global pkg_src therock-%{rocm_release}
%else
%global rocm_release 7.2
%global rocm_patch 2
%global pkg_src rocm-%{rocm_release}.%{rocm_patch}
%endif

%global rocm_version %{rocm_release}.%{rocm_patch}

%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}/
%global pkg_suffix %{rocm_release}
%global pkg_module rocm%{pkg_suffix}
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global pkg_module default
%endif

%if 0%{?suse_version}
%global pkg_name lib%{pkg_library_name}%{pkg_library_version}%{pkg_suffix}
%else
%global pkg_name %{NAME}
%endif

Name:           rocm-core%{pkg_suffix}
Version:        %{rocm_version}
%if %{with preview}
Release:        0%{?dist}
%else
Release:        2%{?dist}
%endif
Summary:        A utility to get the ROCm release version
License:        MIT
URL:            https://github.com/ROCm/rocm-systems
Source0:        %{url}/releases/download/%{pkg_src}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

%if 0%{?suse_version}
Requires:       %{pkg_name}%{?_isa} = %{version}-%{release}
%endif

Provides:       rocm-core = %{version}-%{release}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
%{summary}

%if 0%{?suse_version}
%package -n %{pkg_name}
Summary:        Runtime for %{name}

%description -n %{pkg_name}
%summary

%ldconfig_scriptlets -n %{pkg_name}
%endif

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{pkg_name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%prep
%autosetup -p1 -n %{upstreamname}

%build
%cmake \
    -DROCM_VERSION=%{rocm_version} \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix}

%cmake_build

%install
%cmake_install

rm -rf %{buildroot}/%{pkg_prefix}/.info
rm -rf %{buildroot}/%{pkg_prefix}/%{pkg_libdir}/rocmmod
rm -rf %{buildroot}/%{pkg_prefix}/share/rdhc
# Extra licenses
# Fedora
rm -f %{buildroot}/%{pkg_prefix}/share/doc/*/LICENSE.md
# OpenSUSE
rm -f %{buildroot}/%{pkg_prefix}/share/doc/*/*/LICENSE.md

# Use the system include path
mv  %{buildroot}/%{pkg_prefix}/include/rocm-core/*.h %{buildroot}/%{pkg_prefix}/include/
rm -rf %{buildroot}/%{pkg_prefix}/include/rocm-core

find %{buildroot} -type f -name 'runpath_to_rpath.py' -exec rm {} \;

%if 0%{?suse_version}
%files
%{pkg_prefix}/bin/rdhc
%{pkg_prefix}/libexec/rocm-core/

%files -n %{pkg_name}
%doc README.md
%license LICENSE.md
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so.%{pkg_library_version}{,.*}

%else

%files
%doc README.md
%license LICENSE.md
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so.%{pkg_library_version}{,.*}
%{pkg_prefix}/bin/rdhc
%{pkg_prefix}/libexec/rocm-core/
%endif

%files devel
%{pkg_prefix}/include/*.h
%{pkg_prefix}/%{pkg_libdir}/lib%{pkg_library_name}.so
%{pkg_prefix}/%{pkg_libdir}/cmake/rocm-core/

%changelog
* Fri Apr 17 2026 Tom Rix <Tom.Rix@amd.com> - 7.2.2-2
- Generate suse package name

* Wed Apr 15 2026 Tom Rix <Tom.Rix@amd.com> - 7.2.2-1
- Update to 7.2.2

* Fri Apr 3 2026 Tom Rix <Tom.Rix@amd.com> - 7.2.1-2
- Increment version for devel pkg rename change

* Fri Apr 3 2026 Tom Rix <Tom.Rix@amd.com> - 7.2.1-1
- Update to 7.2.1

* Wed Mar 11 2026 Tom Rix <Tom.Rix@amd.com> - 7.2.0-2
- Add --with preview

* Thu Jan 29 2026 Tom Rix <Tom.Rix@amd.com> - 7.2.0-1
- Update to 7.2.0

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jan 1 2026 Tom Rix <Tom.Rix@amd.com> - 7.1.1-3
- Fix OpenSUSE

* Mon Dec 22 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.1-2
- Add --with compat

* Wed Nov 26 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.1-1
- Update to 7.1.1

* Fri Oct 31 2025 Tom Rix <Tom.Rix@amd.com> - 7.1.0-1
- Update to 7.1.0

* Sat Oct 11 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.2-1
- Update to 7.0.2

* Sat Sep 20 2025 Tom Rix <Tom.Rix@amd.com> - 7.0.1-1
- Update to 7.0.1

* Wed Aug 27 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.3-2
- Add Fedora copyright

* Thu Aug 7 2025 Tom Rix <Tom.Rix@amd.com> - 6.4.3-1
- Update to 6.4.3

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jul 22 2025 Jeremy Newton <alexjnewt at hotmail dot com> - 6.4.2-1
- Update to 6.4.2

* Thu May 22 2025 Jeremy Newton <alexjnewt at hotmail dot com> - 6.4.1-1
- Update to 6.4.1

* Wed Apr 16 2025 Jeremy Newton <alexjnewt at hotmail dot com> - 6.4.0-1
- Update to 6.4.0

* Wed Feb 19 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.3-1
- Update to 6.3.3

* Mon Feb 10 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.2-2
- Fix SLE 15.6

* Wed Jan 29 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.2-1
- Update to 6.3.2

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec 26 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.1-1
- Update to 6.3.1

* Tue Dec 10 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3

