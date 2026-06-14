Name:		    secvarctl
Version:	    1.1.0
Release:	    %autorelease
Summary:	    Suite of tools to manipulate and generate Secure Boot variables on POWER
License:	    Apache-2.0
URL:		    https://github.com/open-power/secvarctl
Source0:	    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/ibm/libstb-secvar/archive/ce98be9d15ac2df062726b4451f0ec0c0b27fbf2.tar.gz

Patch0:         0001-Fix-OpenSSL-4.0-compatibility.patch

BuildRequires:	gcc
BuildRequires:	cmake
BuildRequires:	openssl-devel
BuildRequires:  libasan

Provides:       bundled(libstb-secvar)

%description
Suite of tools to manipulate and generate Secure Boot variables on POWER.

The purpose of this tool is to simplify and automate the process of reading and
writing secure boot keys. secvarctl allows the user to communicate, via terminal
commands, with the keys efficiently. It is supporting automate process of the
both host and guest secure boot keys.

%prep
%autosetup -N
tar xf %{SOURCE1} -C external/libstb-secvar --strip-components=1
%autopatch -p1

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%check
%ifarch ppc64le
make check
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
