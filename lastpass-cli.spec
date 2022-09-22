Name:           lastpass-cli
Version:        1.3.3
Release:        10%{?dist}
Summary:        Command line interface to LastPass.com

License:        GPLv2
URL:            https://github.com/LastPass/lastpass-cli
Source0:        %url/archive/v%{version}/lastpass-cli-%{version}.tar.gz

# RHBZ#1457758
Patch0:         lastpass-cli-1.3.1-remove_reallocarray.patch
# https://github.com/lastpass/lastpass-cli/issues/532
Patch1:         0001-Mark-global-variable-as-extern.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  libxml2-devel
BuildRequires:  libcurl-devel
BuildRequires:  asciidoc
BuildRequires: make
Requires:       pinentry
Requires:       xclip

%description
A command line interface to LastPass.com.

%prep
%autosetup -p1

%build
%cmake .
%make_build

%install
%make_install install-doc

# Install shell completions
install -Dpm0644 contrib/lpass_bash_completion \
    %{buildroot}%{_datadir}/bash-completion/completions/lpass-completion.bash
install -Dpm0644 contrib/completions-lpass.fish \
    %{buildroot}%{_datadir}/fish/vendor_functions.d/lpass.fish
install -Dpm0644 contrib/lpass_zsh_completion \
    %{buildroot}%{_datadir}/zsh/site-functions/_lpass

%files
%license COPYING
%license LICENSE.OpenSSL
%doc README.md
%doc CONTRIBUTING
%doc contrib/examples
%{_bindir}/lpass
%{_mandir}/man1/lpass.1.*
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/lpass-completion.bash
%dir %{_datadir}/fish/vendor_functions.d
%{_datadir}/fish/vendor_functions.d/lpass.fish
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_lpass

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.3.3-8
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 00:29:28 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.3-3
- Better fix for GCC 10

* Thu Jan 23 00:29:28 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.3-2
- Fix compatibility with GCC 10

* Fri Aug 09 17:18:00 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.3-1
- Release 1.3.3 (#1700031)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 24 16:33:41 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.2-1
- Release 1.3.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.1-2
- Remove reallocarray
- Fix RHBZ#1457758

* Mon Jul 02 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.1-1
- Update to version 1.3.1
- Add fish and zsh completions
- Fix #1583717, #1579473, #1459717
- Thanks to Ventz Petkov and Edward J. Huff for their contribution

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 12 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.2-1
- Update to latest 1.1.2 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Mar 6 2016 Tom Prince - 0.9.0-1
- Version number bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 4 2016 Tom Prince - 0.8.0-1
- Version number bump
- Install bash completions

* Thu Dec 24 2015 Tom Prince - 0.7.0-3
- Remove xclip dependency for EPEL.

* Sun Dec 6 2015 Tom Prince - 0.7.0-2
- Address review comments.

* Mon Nov 16 2015 Tom Prince - 0.7.0-1
- Version number bump

* Wed Oct 7 2015 Tom Prince - 0.6.0-1
- Version number bump

* Tue Dec 30 2014 Rohan Ferris - 0.4.0-2
- Include asciidoc

* Tue Dec 30 2014 Rohan Ferris - 0.4.0-1
- Version number bump

* Fri Nov  7 2014 Rohan Ferris
- Initial packaging.
