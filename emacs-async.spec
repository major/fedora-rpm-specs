%global pkg async

Name:           emacs-%{pkg}
Version:        1.9.4
Release:        8%{?dist}
Summary:        Asynchronous processing in Emacs
License:        GPLv2+
URL:            https://github.com/jwiegley/emacs-async
Source0:        %{url}/archive/v%{version}/%{pkg}-%{version}.tar.gz

# Submitted upstream as PR #133.
Patch0: fsf-address.patch
# Fixed upstream with 14f48de586b0.
Patch1: emacs27-makefile.patch

BuildArch:      noarch
BuildRequires:  emacs make
Requires:       emacs(bin) >= %{_emacs_version}

%description
%{name} is a module for doing asynchronous processing in Emacs.

%prep
%autosetup

%build
%make_build

%install
# Async doesn't append the PREFIX on top of DESTDIR when DESTDIR is defined.
mkdir -p %{buildroot}/%{_emacs_sitelispdir}/%{pkg}
make DESTDIR=%{buildroot}/%{_emacs_sitelispdir}/%{pkg} install

%check
emacs --batch -L . -l async-test.el -f async-test-1 -f async-test-2 \
      -f async-test-3 -f async-test-4 -f async-test-5 -f async-test-6

%files
%doc README.md
%{_emacs_sitelispdir}/%{pkg}


%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 12 2020 Tulio Magno Quites Machado Filho <tuliom@ascii.art.br> - 1.9.4-0
- Initial packaging
