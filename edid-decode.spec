%global codate 20230201
%global commit 915b0ce5329f417d2c3f84ddab3d443dd0e01b61
%global shortcommit %(c=%{commit}; echo ${c:0:8})

Name:           edid-decode
Version:        0
Release:        %autorelease -s %{codate}git%{shortcommit}
Summary:        Decode EDID data in human-readable format

License:        MIT
URL:            https://git.linuxtv.org/edid-decode.git/
Source0:        edid-decode-%{shortcommit}.tar.xz
Source1:        edid-decode-snapshot.sh

BuildRequires:  gcc-c++ make

Conflicts:	xorg-x11-utils < 7.5-33

%description
Decodes raw monitor EDID data in human-readable format.


%prep
%setup -q -n %{name}


%build
%set_build_flags
%make_build


%install
%make_install


%files
%doc README
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*


%changelog
%autochangelog
