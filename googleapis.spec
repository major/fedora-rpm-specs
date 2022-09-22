%global commit 7c7a99a90e2d898aad4790107486d3e21167443f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapinfo 20220213git%{shortcommit}
%global debug_package %{nil}

Name:      googleapis
Version:   0
Release:   %autorelease -s %{snapinfo}
Summary:   Public interface definitions of Google APIs
License:   ASL 2.0
URL:       https://github.com/googleapis/googleapis
Source0:   %{URL}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch: noarch

%description
This repository contains the original interface definitions of public Google
APIs that support both REST and gRPC protocols. 
Reading the original interface definitions can provide a better understanding
of Google APIs and help you to utilize them more efficiently.
You can also use these definitions with open source tools to generate client
libraries, documentation, and other artifacts.

%package devel
Summary:   Protocol Buffers definitions of Google APIs

%description devel
This package contains Protocol Buffers definitions of the Google APIs

%prep
%autosetup -n googleapis-%{commit}

%install
for d in $(find google -type d); do
    install --mode 0755 -vd "$d" "%{buildroot}%{_includedir}/$d"
done
for f in $(find google -type f -name "*.proto"); do
    install --mode 0644 -vp "$f" %{buildroot}%{_includedir}/$f
done

%files devel
%license LICENSE
%dir %{_includedir}/google
%{_includedir}/google/*

%changelog
%autochangelog
