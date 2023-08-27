%global commit 7c0562c49e8f33d089f78a76a0f46d8f8a04a9b7
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20201019

Name:           tiosmod
Version:        0.2.7^%{date}g%{shortcommit}
Release:        %autorelease
Summary:        Generic patcher for Texas Instruments calculators

# Building blocks are GPLv2, OS patching logic is WTFPL
License:        GPL-2.0-only AND WTFPL
URL:            https://github.com/debrouxl/tiosmod
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  gcc
Suggests:       rabbitsign

%description
tiosmod is a computer-based unlocking and optimizing program aimed at official
TI-68k calculators OS.

%prep
%autosetup -n %{name}-%{commit}

%build
$CC $CFLAGS -c -o amspatch.o amspatch.c
$CC $CFLAGS -o tiosmod amspatch.o $LDFLAGS

%install
install -Dpm0755 -t %{buildroot}%{_bindir} tiosmod

%files
%license COPYING_GPLv2 COPYING_WTFPLv2
%doc README.txt
%{_bindir}/tiosmod

%changelog
%autochangelog
