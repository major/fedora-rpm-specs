Summary:        Audio and video processing media library
Name:           librem
Version:        2.12.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            https://github.com/baresip/rem
Source0:        https://github.com/baresip/rem/archive/v%{version}/rem-%{version}.tar.gz
BuildRequires:  cmake
%if 0%{?rhel} && 0%{?rhel} < 8
BuildRequires:  cmake3
%endif
BuildRequires:  gcc
BuildRequires:  libre-devel >= 2.12.0
%if 0%{?rhel} == 7
# Atomic support in libre >= 2.1.0
BuildRequires:  devtoolset-8-toolchain
%endif
# Cover multiple third party repositories
Obsoletes:      librem0 < 0.6.0-2
Provides:       librem0 = %{version}-%{release}
Provides:       librem0%{?_isa} = %{version}-%{release}
Obsoletes:      rem < 0.6.0-2
Provides:       rem = %{version}-%{release}
Provides:       rem%{?_isa} = %{version}-%{release}

%description
Librem is an audio and video processing media library. Features are an
audio buffer, audio sample format conversion, audio file reader/writer,
audio mixer, audio resampler, audio tone generator, audio codec (G.711),
DTMF decoder, video mixer, video pixel converter and FIR filter.

%package devel
Summary:        Development files for the rem library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       libre-devel
# Cover multiple third party repositories
Obsoletes:      librem0-devel < 0.6.0-2
Provides:       librem0-devel = %{version}-%{release}
Provides:       librem0-devel%{?_isa} = %{version}-%{release}
Obsoletes:      rem-devel < 0.6.0-2
Provides:       rem-devel = %{version}-%{release}
Provides:       rem-devel%{?_isa} = %{version}-%{release}

%description devel
The librem-devel package includes header files and libraries necessary for
developing programs which use the rem C library.

%prep
%setup -q -n rem-%{version}

%build
%if 0%{?rhel} && 0%{?rhel} < 8
%global cmake %cmake3
%global cmake_build %cmake3_build
%global cmake_install %cmake3_install

. /opt/rh/devtoolset-8/enable
%endif

%cmake \
%if 0%{?rhel} && 0%{?rhel} < 8
  -DOPENSSL_ROOT_DIR:PATH="%{_includedir}/openssl11;%{_libdir}/openssl11"
%endif

%cmake_build

%install
%cmake_install

# Remove static library
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.a

%ldconfig_scriptlets

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_libdir}/%{name}.so.6*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/rem/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Fri Feb 17 2023 Robert Scheck <robert@fedoraproject.org> 2.12.0-1
- Upgrade to 2.12.0 (#2170481)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 14 2023 Robert Scheck <robert@fedoraproject.org> 2.11.0-1
- Upgrade to 2.11.0 (#2160251)

* Wed Dec 07 2022 Robert Scheck <robert@fedoraproject.org> 2.10.0-1
- Upgrade to 2.10.0 (#2151700)

* Tue Nov 01 2022 Robert Scheck <robert@fedoraproject.org> 2.9.0-1
- Upgrade to 2.9.0 (#2139164)

* Sat Oct 01 2022 Robert Scheck <robert@fedoraproject.org> 2.8.0-1
- Upgrade to 2.8.0 (#2131445)

* Thu Sep 01 2022 Robert Scheck <robert@fedoraproject.org> 2.7.0-1
- Upgrade to 2.7.0 (#2123484)

* Wed Aug 03 2022 Robert Scheck <robert@fedoraproject.org> 2.6.0-2
- Rebuilt for libre 2.6.1

* Mon Aug 01 2022 Robert Scheck <robert@fedoraproject.org> 2.6.0-1
- Upgrade to 2.6.0 (#2112886)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 02 2022 Robert Scheck <robert@fedoraproject.org> 2.5.0-1
- Upgrade to 2.5.0 (#2103280)

* Wed Jun 01 2022 Robert Scheck <robert@fedoraproject.org> 2.4.0-1
- Upgrade to 2.4.0 (#2092575)

* Mon May 02 2022 Robert Scheck <robert@fedoraproject.org> 2.3.0-1
- Upgrade to 2.3.0 (#2080806)

* Sat Apr 09 2022 Robert Scheck <robert@fedoraproject.org> 2.0.1-1
- Upgrade to 2.0.1 (#2073698)

* Mon Mar 28 2022 Robert Scheck <robert@fedoraproject.org> 2.0.0-2
- Rebuilt for libre 2.2.0

* Sun Mar 13 2022 Robert Scheck <robert@fedoraproject.org> 2.0.0-1
- Upgrade to 2.0.0 (#2063450)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Apr 10 2021 Robert Scheck <robert@fedoraproject.org> 1.0.0-1
- Upgrade to 1.0.0 (#1948096)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 10 2020 Robert Scheck <robert@fedoraproject.org> 0.6.0-4
- Rebuilt for libre 1.1.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 28 2020 Robert Scheck <robert@fedoraproject.org> 0.6.0-2
- Changes to match the Fedora Packaging Guidelines (#1843268 #c1)

* Thu May 28 2020 Robert Scheck <robert@fedoraproject.org> 0.6.0-1
- Upgrade to 0.6.0 (#1843268)
- Initial spec file for Fedora and Red Hat Enterprise Linux
