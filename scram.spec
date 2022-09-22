%global    enable_tests 0

Name:       scram
Version:    0.16.2
Release:    15%{?dist}
Summary:    Probabilistic Risk Analysis Tool

License:    GPLv3+
Url:        https://scram-pra.org
Source0:    https://github.com/rakhimov/scram/archive/%{version}.tar.gz
Source1:    %{name}.1

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.8.0
BuildRequires:  boost-devel >= 1.61.0
BuildRequires:  libxml2-devel
BuildRequires:  gperftools-devel
%if 0%{?enable_tests}
BuildRequires:  catch-devel
BuildRequires:  jemalloc-devel
%endif
BuildRequires:  cmake(Qt5)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  desktop-file-utils

%description
A command line probabilistic risk analysis tool
capable of performing event tree analysis,
static fault tree analysis,
analysis with common cause failure models,
probability calculations with importance analysis,
and uncertainty analysis with Monte Carlo simulations.

%package gui
Summary:    GUI for Probabilistic Risk Analysis Tool
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description gui
scram GUI.

%prep
%autosetup
# Fix build with boost 1.73
sed -i 's|BOOST_THROW_EXCEPTION_CURRENT_FUNCTION|BOOST_CURRENT_FUNCTION|' src/error.h

%build
export CXXFLAGS="%{__global_compiler_flags} -I/usr/include/catch"
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if 0%{?enable_tests}
    -DBUILD_TESTING=ON \
%endif
    %{nil}
%cmake_build

%install
%cmake_install
install -p -D -m 644 %{SOURCE1} -t %{buildroot}%{_mandir}/man1/
install -p -D -m 644 scripts/%{name} %{buildroot}%{_datadir}/bash-completion/completions/%{name}
%if 0%{?enable_tests}
    rm %{buildroot}%{_bindir}/%{name}_tests
    rm %{buildroot}%{_bindir}/%{name}gui_test*
%endif
sed -i '/URL/d' %{buildroot}%{_datadir}/applications/%{name}-gui.desktop

%check
%if 0%{?enable_tests}
    mkdir build/share/%{name}
    cp share/* build/share/%{name}
    pushd build
        ./bin/%{name}_tests -e
    popd
%endif
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-gui.desktop


%files
%doc doc/*
%license LICENSE
%{_bindir}/%{name}
%{_prefix}/lib/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}
%{_datadir}/bash-completion/completions/%{name}

%files gui
%{_bindir}/%{name}-gui
%{_datadir}/applications/%{name}-gui.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.16.2-14
- Rebuilt for Boost 1.78

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 0.16.2-12
- Rebuilt for Boost 1.76

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.16.2-9
- Rebuilt for Boost 1.75

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 0.16.2-7
- Rebuilt for Boost 1.73

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 0.16.2-3
- Rebuilt for Boost 1.69

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 16 2018 Vasiliy N. Glazov <vascom2@gmail.com> - 0.16.2-1
- Update to 0.16.2
- Enable tests
- Build with GUI

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.13.0-7
- Rebuilt for Boost 1.66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 0.13.0-4
- Rebuilt for s390x binutils bug

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 0.13.0-3
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri May 12 2017 Olzhas Rakhimov <ol.rakhimov@gmail.com> - 0.13.0-1
- Update to new upstream 0.13.0
- Change the tarball source to GitHub
- Bump Boost min version to 1.58
- Include help2man generated man page

* Sun Mar 19 2017 Olzhas Rakhimov <ol.rakhimov@gmail.com> - 0.12.0-1
- Initial RPM Package
