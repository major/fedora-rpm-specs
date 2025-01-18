%global bashcompdir %(pkg-config --variable=completionsdir bash-completion)
%global zshcompdir %{_datadir}/zsh/site-functions

Name: creds
Version: 0.1.0
Release: 15%{?dist}
Summary: Simple encrypted credential management with GPG

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: https://github.com/joemiller/creds
Source0: https://github.com/joemiller/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: bash-completion

Requires: gnupg2

%description
Simple encrypted credential management with GPG.


%prep
%autosetup
# Remove shebang from Bash completion file.
sed -i -e '/^#!\//, 1d' completions/bash/_%{name}.sh


%build


%install
# NOTE: creds comes with a Makefile, but the paths therein are hard-coded which
# makes it unsuitable for RPM packaging purposes.
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 %{name} %{buildroot}%{_bindir}

# Install Bash/Zsh completion files.
mkdir -p %{buildroot}%{bashcompdir}
mv completions/bash/_%{name}.sh %{buildroot}%{bashcompdir}/%{name}
mkdir -p %{buildroot}%{zshcompdir}
mv completions/zsh/_%{name}.sh %{buildroot}%{zshcompdir}/_%{name}


%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{bashcompdir}/%{name}
# Since Zsh is not a requirement for this package, it must own all the
# directories below %%{_datadir} to avoid unowned directories.
# https://docs.fedoraproject.org/en-US/packaging-guidelines/UnownedDirectories/
%dir %(dirname %{zshcompdir})
%dir %{zshcompdir}
%{zshcompdir}/_%{name}


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.0-14
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Tadej Janež <tadej.j@nez.si> - 0.1.0-1
- Initial package
