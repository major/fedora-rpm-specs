Name:           TE2PE
Version:        0.1.1
Release:        %autorelease
Summary:        Primitive TE to PE32 converter 

License:        WTFPL
URL:            https://github.com/LongSoft/TE2PE
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc

%description
This program tries to convert Terse Executable image used to store PEI modules
in different UEFI-compatible firmwares into normal PE32(+) image

%prep
%autosetup

%build
$CC $CFLAGS %{name}.c -o %{name} $LDFLAGS

%install
install -Dpm0755 -t %{buildroot}%{_bindir} %{name}

%files
%doc README.md
%{_bindir}/TE2PE

%changelog
%autochangelog
