# Google does not properly version the sources, this commit is the "tag-release" of this package
%global srcname compute-image-packages
%global commit 3178e68b004eea38dada580de4193994f45dfc50
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           google-compute-engine-oslogin
Version:        1.4.3
Release:        18%{?dist}
Summary:        OS Login Functionality for Google Compute Engine

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/GoogleCloudPlatform/%{srcname}
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pam-devel
BuildRequires:  selinux-policy, selinux-policy-devel

Requires(post): selinux-policy-base >= %{_selinux_policy_version}
Requires(post): policycoreutils
Requires(post): policycoreutils-python-utils
Requires(pre):  libselinux-utils
Requires(post): libselinux-utils

%description
This package contains several libraries and changes to enable OS Login
functionality for Google Compute Engine.

%prep
%autosetup -n %{srcname}-%{commit}

# Delete pregenerated SELinux policy module file
rm google_compute_engine_oslogin/policy/oslogin.pp

%build
pushd google_compute_engine_oslogin
# Hack to make compile flags work with horrid Makefile
export CC="gcc %{optflags}"
export CXX="g++ %{optflags}"
%make_build LIBS="-lcurl -ljson-c"

# Build the SELinux policy module
make -C policy
popd

%install
pushd google_compute_engine_oslogin
%make_install NSS_INSTALL_PATH=%{_libdir} PAM_INSTALL_PATH=%{_libdir}/security INSTALL_SELINUX=true
popd

# Compress the policy module
bzip2 -9 %{buildroot}%{_datadir}/selinux/packages/oslogin.pp

# Change all the libraries to be executable
chmod +x %{buildroot}%{_libdir}/*.so*
chmod +x %{buildroot}%{_libdir}/security/*.so*

# Make the directory managed by this package...
mkdir -p %{buildroot}%{_localstatedir}/google-sudoers.d

%files
%license LICENSE
%doc google_compute_engine_oslogin/README.md
%{_libdir}/libnss_cache_oslogin.so.*
%{_libdir}/libnss_oslogin.so.*
%{_libdir}/libnss_cache_%{name}-%{version}.so
%{_libdir}/libnss_%{name}-%{version}.so
%{_libdir}/security/pam_oslogin_admin.so
%{_libdir}/security/pam_oslogin_login.so
%{_bindir}/google_authorized_keys
%{_bindir}/google_oslogin_control
%{_bindir}/google_oslogin_nss_cache
%{_datadir}/selinux/packages/oslogin.pp.bz2
%dir %{_localstatedir}/google-sudoers.d

%post
%selinux_modules_install %{_datadir}/selinux/packages/oslogin.pp.bz2

%postun
%selinux_modules_uninstall oslogin

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.3-17
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Björn Esser <besser82@fedoraproject.org> - 1.4.3-8
- Rebuild for versioned symbols in json-c

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 1.4.3-5
- Rebuild (json-c)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Neal Gompa <ngompa13@gmail.com> - 1.4.3-1
- Rebase to 1.4.3

* Tue Oct 30 2018 Neal Gompa <ngompa13@gmail.com> - 1.3.1-1
- Initial packaging for Fedora
