Name:           wlrctl
Version:        0.2.2
Release:        4%{?dist}
Summary:        Manipulate Wayland compositors using wlroots protocols

License:        MIT
URL:            https://git.sr.ht/~brocellous/wlrctl
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary}.


%prep
%autosetup -n %{name}-v%{version} -p1

# Disable Werror
sed -e "/werror=true/d" -i meson.build


%build
%meson
%meson_build


%install
%meson_install


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/zsh/site-functions/_wlrctl
%{_mandir}/man1/wlrctl.1*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.2.2-1
- Initial package
