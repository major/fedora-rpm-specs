%{?mingw_package_header}

%global date 20260212
%global commit 2977346e6c458a345976688844740704860a83b9
%global shortcommit 2977346e

Name:           mingw-devcon
Version:        0~%{date}git%{shortcommit}
Release:        6%{?dist}
Summary:        Tool to display and manipulate Windows devices

# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/thread/ZSVCFJFVMLTODFKGV352TYHH5ZQODJXD/
License:        MS-PL
BuildArch:      noarch

URL:            https://github.com/microsoft/Windows-driver-samples
# Note: Only the setup/devcon subdirectory is packaged.
# git archive --format=tar --prefix=devcon/ HEAD setup/devcon/ | gzip -c
Source0:        devcon%{shortcommit}.tar.gz
Source1:        https://github.com/microsoft/Windows-driver-samples/raw/refs/heads/main/LICENSE
Source2:        Makefile

# Fix an error message in devcon.
# https://github.com/microsoft/Windows-driver-samples/pull/1350
Patch1:         0001-devcon-In-MSG_FAILURE-show-the-cmd-name.patch

BuildRequires:  make

# Older versions of the toolchain miscompiled this program.  All
# strings were printed as single characters, presumably because of
# UTF-16LE vs ASCII confusion.  Make sure we are using a sufficiently
# new toolchain.
BuildRequires:  mingw32-binutils >= 2.45.1
BuildRequires:  mingw32-gcc-c++ >= 15.2.1
BuildRequires:  mingw64-binutils >= 2.45.1
BuildRequires:  mingw64-gcc-c++ >= 15.2.1


%description
DevCon is a Microsoft Windows command-line tool that displays detailed
information about devices, and lets you search for and manipulate devices
from the command line. DevCon enables, disables, installs, configures,
and removes devices on the local computer and displays detailed information
about devices on local and remote computers. DevCon is included in the WDK.


%package -n mingw32-devcon
Summary:        Tool to display and manipulate Windows devices


%description -n mingw32-devcon
Tool to display and manipulate Windows devices


%package -n mingw64-devcon
Summary:        Tool to display and manipulate Windows devices


%description -n mingw64-devcon
Tool to display and manipulate Windows devices


%{?mingw_debug_package}


%package redistributable
Summary:        Tool to display and manipulate Windows devices


%description redistributable
Tool to display and manipulate Windows devices.

This package contains the binaries without any mingw toolchain
dependencies, for use with virt-v2v.


%prep
%autosetup -n devcon -p1
cp %{SOURCE1} LICENSE
cp %{SOURCE2} Makefile


%build
mkdir x86 x64
pushd x86
make -f ../Makefile BITS=32 srcdir=../setup/devcon all
popd
pushd x64
make -f ../Makefile BITS=64 srcdir=../setup/devcon all
popd


%install
mkdir -p $RPM_BUILD_ROOT%{mingw32_bindir}/
%{__install} x86/devcon.exe $RPM_BUILD_ROOT%{mingw32_bindir}/
mkdir -p $RPM_BUILD_ROOT%{mingw64_bindir}/
%{__install} x64/devcon.exe $RPM_BUILD_ROOT%{mingw64_bindir}/
# redistributable
mkdir -p $RPM_BUILD_ROOT%{_datadir}/virt-tools/{x86,x64}/
%{__install} x86/devcon.exe $RPM_BUILD_ROOT%{_datadir}/virt-tools/x86/
%{__install} x64/devcon.exe $RPM_BUILD_ROOT%{_datadir}/virt-tools/x64/


%files -n mingw32-devcon
%doc setup/devcon/README.md
%license LICENSE
%{mingw32_bindir}/devcon.exe


%files -n mingw64-devcon
%doc setup/devcon/README.md
%license LICENSE
%{mingw64_bindir}/devcon.exe


%files redistributable
%doc setup/devcon/README.md
%license LICENSE
%dir %{_datadir}/virt-tools/
%dir %{_datadir}/virt-tools/x86/
%dir %{_datadir}/virt-tools/x64/
%{_datadir}/virt-tools/x86/devcon.exe
%{_datadir}/virt-tools/x64/devcon.exe
# duplicate debuginfo
%exclude /usr/lib/debug%{_datadir}/virt-tools/*/*.debug


%changelog
* Thu Feb 26 2026 Richard W.M. Jones <rjones@redhat.com> - 0-6
- Fix Makefile so it includes the whole message catalog

* Mon Feb 23 2026 Richard W.M. Jones <rjones@redhat.com> - 0-5
- Initial packaging (RHBZ#2440652)
- Link the binaries statically so they don't require libstdc++.dll
- Compile resource catalog and link it
- Include a Makefile for easier building
- Add patch to fix an error message
