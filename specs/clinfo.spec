Name:           clinfo
Summary:        Enumerate OpenCL platforms and devices
Version:        3.0.25.02.14
Release:        %autorelease
# Automatically converted from old format: CC0 - review is highly recommended.
License:        CC0-1.0
URL:            https://github.com/Oblomov/clinfo
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ocl-icd-devel

%description
A simple OpenCL application that enumerates all possible platform and
device properties. Inspired by AMD's program of the same name, it is
coded in pure C99 and it tries to output all possible information,
including that provided by platform-specific extensions, and not to
crash on platform-unsupported properties (e.g. 1.2 properties on 1.1
platforms).

%prep
%autosetup

%build
%set_build_flags
%make_build

%install
install -Dpm0755 -t %{buildroot}%{_bindir} %{name}
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 man1/%{name}.1

%files
%license LICENSE legalcode.txt
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
