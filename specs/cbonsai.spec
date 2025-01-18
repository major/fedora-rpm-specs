Name:           cbonsai
Version:        1.3.1
Release:        8%{?dist}
Summary:        Grow bonsai trees in your terminal

License:        GPL-3.0-only
URL:            https://gitlab.com/jallbrit/cbonsai
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  scdoc

%description
cbonsai is a bonsai tree generator, written in C using ncurses. It
intelligently creates, colors, and positions a bonsai tree, and is
entirely configurable via CLI options-- see usage. There are 2 modes of
operation: static (see finished bonsai tree), and live (see growth step-by-
step).


%prep
%autosetup -n %{name}-v%{version}


%build
%if 0%{?rhel} || 0%{?fedora} == 35
%set_build_flags
%endif
%make_build


%install
%make_install PREFIX=%{_prefix}


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 17 2022 Jonathan Wright <jonathan@almalinux.org> - 1.3.1-2
- Update spec to build on epel and f35

* Mon Aug 15 2022 Jonathan Wright <jonathan@almalinux.org> - 1.3.1-1
- Initial package build
