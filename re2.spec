%global longver 2022-06-01
%global shortver %(echo %{longver}|sed 's|-||g')

Name:           re2
Version:        %{shortver}
Epoch:          1
Release:        4%{?dist}
Summary:        C++ fast alternative to backtracking RE engines
License:        BSD
URL:            http://github.com/google/%{name}/
Source0:        https://github.com/google/re2/archive/%{longver}.tar.gz

BuildRequires: cmake
BuildRequires:  gcc-c++
%description
RE2 is a C++ library providing a fast, safe, thread-friendly alternative to
backtracking regular expression engines like those used in PCRE, Perl, and
Python.

Backtracking engines are typically full of features and convenient syntactic
sugar but can be forced into taking exponential amounts of time on even small
inputs.

In contrast, RE2 uses automata theory to guarantee that regular expression
searches run in time linear in the size of the input, at the expense of some
missing features (e.g back references and generalized assertions).

%package        devel
Summary:        C++ header files and library symbolic links for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel
This package contains the C++ header files and symbolic links to the shared
libraries for %{name}. If you would like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q -n %{name}-%{longver}

%build
# The RPM macro for the linker flags does not exist on EPEL
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro}

%cmake . \
    -DOVERRIDE_INSTALL_PREFIX=/usr \
    -DCMAKE_COLOR_MAKEFILE:BOOL=OFF \
    -DINSTALL_LIBDIR:PATH=%{_libdir} \
    "-GUnix Makefiles"

%cmake_build

%install
%cmake_install

# Suppress the static library
rm -fv %{buildroot}%{_libdir}/libre2.a

mkdir -p %{buildroot}%{_libdir}/pkgconfig/

# This gets done in Makefile, but nothing in CMake build does it:
# https://github.com/google/re2/issues/349
sed -i -e 's,@includedir@,%{_includedir},g' re2.pc
sed -i -e 's,@libdir@,%{_libdir},g' re2.pc
install -m 0644 re2.pc %{buildroot}%{_libdir}/pkgconfig/

%check
%make_build shared-test

%ldconfig_scriptlets

%files
%license LICENSE
%doc AUTHORS CONTRIBUTORS README
%{_libdir}/libre2.so.9*

%files devel
%{_includedir}/re2/
%{_libdir}/libre2.so
%{_libdir}/pkgconfig/re2.pc
%{_libdir}/cmake/re2/*.cmake

%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:20220601-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:20220601-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:20220601-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 30 2022 Denis Arnaud <denis.arnaud_fedora@m4x.org>  - 1:20220601-1
- Upgrade to 2022-06-01

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:20211101-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:20211101-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Adam Williamson <awilliam@redhat.com> - 1:20211101-2
- Backport patch to fix thread dependency discovery
- Substitute the pkgconfig file before installing it (#2038572)
- Drop soname patches as upstream seems to be doing it properly now

* Fri Jan 07 2022 Denis Arnaud <denis.arnaud_fedora@m4x.org>  - 1:20211101-1
- Upgrade to 2021-11-01

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 1:20190801-8
- Rebuilt for removed libstdc++ symbol (#1937698)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:20190801-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 26 2020 Jeff Law <law@redhat.com> - 1:20190801-6
- No longer force C++11

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:20190801-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:20190801-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 14 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:20190801-3
- -devel: use epoch in versioned dep

* Wed Aug 14 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:20190801-2
- bump soname
- tighten %%files, track soname explicitly
- use %%make_build %%make_install macros
- Epoch:1 for upgrade path (from f29)

* Sat Aug 03 2019 Lukas Vrabec <lvrabec@redhat.com> - 20190801-1
- update to 20190801

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20160401-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20160401-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20160401-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20160401-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20160401-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20160401-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20160401-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 29 2016 Tom Callaway <spot@fedoraproject.org> - 20160401-2
- hardcode -std=c++11 for older compilers

* Fri Apr 29 2016 Tom Callaway <spot@fedoraproject.org> - 20160401-1
- update to 20160401

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20131024-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20131024-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 15 2015 Petr Pisar <ppisar@redhat.com> - 20131024-4
- Rebuild owing to C++ ABI change in GCC-5 (bug #1195351)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20131024-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20131024-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 11 2013 Tom Callaway <spot@fedoraproject.org> - 20131024-1
- update to 20131024
- fix symbols export to stop test from failing

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130115-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 17 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> 20130115-2
- Took into account the feedback from review request (#868578).

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> 20130115-1
- The download source comes now directly from the project.

* Thu Oct 25 2012 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.0.0-2
- Took into account review request (#868578) feedback.

* Sat Oct 20 2012 Denis Arnaud <denis.arnaud_fedora@m4x.org> 0.0.0-1
- RPM release for Fedora 18

