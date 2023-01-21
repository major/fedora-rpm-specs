%{?nodejs_default_filter}

%define pkg_name diagnostic-languageserver

Name:           nodejs-diagnostic-language-server
Version:        1.13.0
Release:        4%{?dist}
Summary:        Diagnostic language server that integrate with linters
License:        MIT
Url:            https://github.com/iamcco/diagnostic-languageserver
Source0:        %{url}/archive/v%{version}/%{pkg_name}-%{version}.tar.gz
# Create with `bash prepare_vendor.sh`
Source1:        %{pkg_name}-%{version}-vendor.tar.xz
BuildRequires:  coffee-script
BuildRequires:  fdupes
BuildRequires:  nodejs-typescript
BuildRequires:  nodejs-packaging
BuildRequires:  npm >= 14
BuildRequires:  perl-interpreter
BuildRequires:  rsync
BuildRequires:  yarnpkg
BuildArch:      noarch

%description
General purpose Language Server that integrate with linters to support
diagnostic features.

For example:
* ShellCheck
* yamllint
* languagetool

%prep
%autosetup -n %{pkg_name}-%{version} -a1 -p1

%build
export YARN_CACHE_FOLDER="$(pwd)/.package-cache"
yarn install --offline

npm run build

%install
export YARN_CACHE_FOLDER="$(pwd)/.package-cache"

# Only install production dependencies in node_modules
yarn install --production --offline

for S in $(grep -l '#!.*node' \
    bin/* \
    node_modules/rimraf/bin.js \
    node_modules/vscode-languageserver/bin/* \
    ) ; do
    SB="${S}.backup"
    cp ${S} ${SB}
    perl -p -i -e 's|#!/usr/bin/env node|#!%{_bindir}/node|g' $S
    diff -urN ${SB} ${S} || :
    rm ${SB}
done

install -d -m 0755 %{buildroot}%{_bindir}
ln -s %{nodejs_sitelib}/%{pkg_name}/bin/index.js %{buildroot}%{_bindir}/%{pkg_name}

install -d -m 0755 %{buildroot}%{nodejs_sitelib}/%{pkg_name}/
rsync -av --exclude=test * %{buildroot}%{nodejs_sitelib}/%{pkg_name}/

find %{buildroot}%{nodejs_sitelib}/%{pkg_name} -name "*.bak" -delete
find %{buildroot}%{nodejs_sitelib}/%{pkg_name} -type f -name "\.*" -delete

%fdupes %{buildroot}%{nodejs_sitelib}/%{pkg_name}

%files
%license LICENSE
%doc README.md
%dir %{nodejs_sitelib}
%{_bindir}/%{pkg_name}
%{nodejs_sitelib}/%{pkg_name}/

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 26 2021 Pavel Filipenský <pfilipen@redhat.com> - 1.13.0-1
- Update to version 1.13.0

* Mon Aug 09 2021 Andreas Schneider <asn@redhat.com> - 1.12.0-1
- Initial package
