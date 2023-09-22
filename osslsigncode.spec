%if 0%{?rhel}
%bcond_with tests
%else
%ifarch s390x
%bcond_with tests
%else
# Disable tests since 2.3 version due
# https://github.com/mtrojnar/osslsigncode/issues/140#issuecomment-1060636197
%bcond_with tests
%endif
%endif

Name:       osslsigncode
Version:    2.7
Release:    %autorelease
Summary:    OpenSSL based Authenticode signing for PE/MSI/Java CAB files

License:    GPLv3+
URL:        https://github.com/mtrojnar/osslsigncode
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# To prevent network access during tests
# Patch0:     %{name}-preventnetwork-access-during-tests.patch

BuildRequires: coreutils
BuildRequires: gcc
BuildRequires: cmake >= 3.17
BuildRequires: sed

BuildRequires: pkgconfig(libcrypto) >= 1.1.0
BuildRequires: pkgconfig(libcurl) >= 7.12.0
BuildRequires: pkgconfig(openssl) >= 1.1.0
BuildRequires: pkgconfig(zlib)

%if %{with tests}
BuildRequires: gcab
BuildRequires: java-1.8.0-openjdk-headless
BuildRequires: libfaketime
BuildRequires: mingw64-gcc
BuildRequires: msitools
BuildRequires: openssl >= 1.1.0
BuildRequires: vim-common
%endif

%description
osslsigncode is a small tool that implements part of the functionality of the
Microsoft tool signtool.exe - more exactly the Authenticode signing and
timestamping. But osslsigncode is based on OpenSSL and cURL, and thus should
be able to compile on most platforms where these exist.


%prep
%autosetup


%build
%cmake
%cmake_build


%install
%cmake_install


%check
# https://bugzilla.redhat.com/show_bug.cgi?id=1882547#c2
%if %{with tests}
%ctest
%endif


%files
%license LICENSE.txt COPYING.txt
%doc README.md NEWS.md TODO.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/*.bash
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions


%changelog
%autochangelog
