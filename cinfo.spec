Name:           cinfo
Version:        0.4.9
Release:        1%{?dist}
Summary:        Fast and minimal system information tool

License:        GPL-3.0-only
URL:            https://github.com/mrdotx/cinfo
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
%{summary}

%prep
%autosetup


%build
%set_build_flags
%make_build


%install
%make_install PREFIX=%{_prefix}


%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Tue Aug 30 2022 Jonathan Wright <jonathan@almalinux.org> 0.4.9-1
- update to 0.4.9
- rhbz#2121986

* Sat Aug 20 2022 Jonathan Wright <jonathan@almalinux.org> 0.4.8-1
- Initial package build
- rhbz#2120002
