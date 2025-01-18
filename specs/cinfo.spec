Name:           cinfo
Version:        0.5.10
Release:        2%{?dist}
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
# remove lines that build for pacman
sed -i -e '/\*PKGS_CMD/d' -e '/\*PKGS_DESC/d' config.def.h
# add lines to build for dnf
cat >> config.def.h << EOL
static const char *PKGS_CMD             = "rpm -qa | wc -l",
                  *PKGS_DESC            = " [dnf]";
EOL

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
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 08 2024 Jonathan Wright <jonathan@almalinux.org> - 0.5.10-1
- update to 0.5.10 rhbz#2278805

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 06 2024 Jonathan Wright <jonathan@almalinux.org> - 0.5.5-1
- update to 0.5.5 rhbz#2262896

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec 14 2023 Jonathan Wright <jonathan@almalinux.org> - 0.5.4-1
- Update to 0.5.4
- Patch compile to look for rpm packages, not pacman rhbz#2254464

* Fri Aug 04 2023 Jonathan Wright <jonathan@almalinux.org> - 0.5.2-1
- Update to 0.5.2 rhbz#2223912

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 07 2022 Jonathan Wright <jonathan@almalinux.org> 0.5.1-1
- update to 0.5.1 rhbz#2140024

* Tue Oct 11 2022 Jonathan Wright <jonathan@almalinux.org> 0.5.0-1
- update to 0.5.0 rhbz#2133897

* Tue Aug 30 2022 Jonathan Wright <jonathan@almalinux.org> 0.4.9-1
- update to 0.4.9
- rhbz#2121986

* Sat Aug 20 2022 Jonathan Wright <jonathan@almalinux.org> 0.4.8-1
- Initial package build
- rhbz#2120002
