%global pkg epc

Name:           emacs-%{pkg}
Version:        0.1.1
Release:        7%{?dist}
Summary:        A RPC stack for Emacs Lisp

License:        GPLv3+
URL:            https://github.com/kiwanami/%{name}/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Fix make-network-process to work with Emacs >= 26
Patch0:         %{name}-0.1.1-asyncness.patch

BuildRequires:  emacs
BuildRequires:  emacs-ctable
BuildRequires:  emacs-deferred
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-ctable
Requires:       emacs-deferred
BuildArch:      noarch

%description
This program is an asynchronous RPC stack for Emacs. Using this RPC stack, the
Emacs can communicate with the peer process smoothly. Because the protocol
employs S-expression encoding and consists of asynchronous communications, the
RPC response is fairly good.


%prep
%autosetup


%build
%{_emacs_bytecompile} %{pkg}.el %{pkg}s.el


%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* %{pkg}s.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/


%check
emacs --batch -q --no-site-file --no-splash \
    -L $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/ \
    -l test-%{pkg}.el \
    -f cc:test-all


%files
%doc readme.md
%{_emacs_sitelispdir}/%{pkg}/


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 10 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.1.1-4
- Fix make-network-process to work with Emacs >= 26
- Add tests

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.1.1-1
- Initial RPM release
