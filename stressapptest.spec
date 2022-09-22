%global forgeurl https://github.com/stressapptest/stressapptest
%global commit 6714c57d0d67f5a2a7a9987791af6729289bf64e
%forgemeta

Name:           stressapptest
Version:        1.0.9
Release:        %autorelease
Summary:        Stressful Application Test - userspace memory and IO test

License:        ASL 2.0
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  make

%description
Stressful Application Test (or stressapptest, its unix name) is a memory
interface test. It tries to maximize randomized traffic to memory from
processor and I/O, with the intent of creating a realistic high load situation
in order to test the existing hardware devices in a computer. It has been used
at Google for some time and now it is available under the Apache 2.0 license.

%prep
%forgesetup

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING NOTICE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
