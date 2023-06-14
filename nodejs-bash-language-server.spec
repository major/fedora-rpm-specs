%{?nodejs_default_filter}

%define pkg_name bash-language-server

Name:           nodejs-bash-language-server
Version:        4.10.0
Release:        1%{?dist}
Summary:        A language server for Bash
License:        MIT
Url:            https://github.com/bash-lsp/bash-language-server
Source0:        %{url}/archive/server-%{version}/%{pkg_name}-%{version}.tar.gz
# Create with `bash prepare_vendor.sh`
Source1:        %{pkg_name}-%{version}-vendor.tar.xz
BuildRequires:  fdupes
BuildRequires:  nodejs-typescript
BuildRequires:  nodejs-packaging
BuildRequires:  npm
BuildRequires:  perl-interpreter
BuildRequires:  rsync
BuildRequires:  yarnpkg
BuildArch:      noarch
ExclusiveArch: %{nodejs_arches} noarch
Recommends:     ShellCheck

%description
Bash language server implementation based on Tree Sitter and its grammar for
Bash with explainshell integration.

%prep
%autosetup -n %{pkg_name}-server-%{version} -a1 -p1

%build
export YARN_CACHE_FOLDER="$(pwd)/.package-cache"
yarn install --offline --frozen-lockfile

npm run compile

%install
export YARN_CACHE_FOLDER="$(pwd)/.package-cache"

# Only install production dependencies in node_modules
yarn install --production --offline --frozen-lockfile

for S in $(grep -l '#!.*node' \
    server/bin/* \
    server/node_modules/acorn/bin/* \
    server/node_modules/ajv/scripts/* \
    server/node_modules/escodegen/bin/* \
    server/node_modules/esprima/bin/* \
    server/node_modules/performance-now/test/scripts/* \
    server/node_modules/pn/scripts/* \
    server/node_modules/sshpk/bin/* \
    server/node_modules/uuid/bin/* \
    server/node_modules/vscode-languageserver/bin/* \
    ) ; do
        SB="${S}.backup"
        cp ${S} ${SB}
        perl -p -i -e 's|#!/usr/bin/env node|#!%{_bindir}/node|g' $S
        diff -urN ${SB} ${S} || :
        rm ${SB}
done

install -d -m 0755 %{buildroot}%{_bindir}

cat << EOF > %{buildroot}%{_bindir}/%{pkg_name}
#!/bin/sh
export NODE_ENV=production

exec /usr/bin/node %{nodejs_sitelib}/%{pkg_name}/out/cli.js "\$@"
EOF
chmod +x %{buildroot}%{_bindir}/%{pkg_name}

install -d -m 0755 %{buildroot}%{nodejs_sitelib}/%{pkg_name}/
rsync -av server/ %{buildroot}%{nodejs_sitelib}/%{pkg_name}/

rm -rf %{buildroot}%{nodejs_sitelib}/%{pkg_name}/node_modules/performance-now/test/
chmod 0644 %{buildroot}%{nodejs_sitelib}/%{pkg_name}/tree-sitter-bash.wasm \
    %{buildroot}%{nodejs_sitelib}/%{pkg_name}/node_modules/web-tree-sitter/tree-sitter.wasm

find %{buildroot}%{nodejs_sitelib}/%{pkg_name} -name "*.bak" -delete
find %{buildroot}%{nodejs_sitelib}/%{pkg_name} -type f -name "\.*" -delete


%fdupes %{buildroot}%{nodejs_sitelib}/%{pkg_name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{pkg_name}
%{nodejs_sitelib}/%{pkg_name}/

%changelog
* Mon Jun 12 2023 Pavel Filipenský <pfilipen@redhat.com> - 4.6.10-1
- Update to version 4.10.0 - https://github.com/bash-lsp/bash-language-server/blob/server-4.10.0/server/CHANGELOG.md

* Thu Feb 02 2023 Pavel Filipenský <pfilipen@redhat.com> - 4.6.1-2
- Fix /usr/bin/bash-language-server

* Mon Jan 30 2023 Pavel Filipenský <pfilipen@redhat.com> - 4.6.1-1
- Update to version 4.6.1
  * https://github.com/bash-lsp/bash-language-server/blob/server-4.6.1/server/CHANGELOG.md

* Sun Jan 29 2023 Jonathan Lebon <jonathan@jlebon.com> - 3.2.0-3
- Don't own /usr/lib/node_modules

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 19 2022 Pavel Filipenský <pfilipen@redhat.com> - 3.0.5-1
- Update to version 3.0.5
  * https://github.com/bash-lsp/bash-language-server/blob/server-3.0.5/server/CHANGELOG.md
- Linting based on shellcheck
- Update bashls-fix-CVE-2022-0613.patch with content of https://patch-diff.githubusercontent.com/raw/bash-lsp/bash-language-server/pull/489.patch

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 17 2022 Pavel Filipenský <pfilipen@redhat.com> - 2.0.0-3
- resolves: #2055544 - Fix CVE-2022-0613

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 26 2021 Pavel Filipenský <pfilipen@redhat.com> - 2.0.0-1
- Update to version 2.0.0
  * https://github.com/bash-lsp/bash-language-server/blob/server-2.0.0/server/CHANGELOG.md
- Fixed indentation for node shebang loop

* Thu Aug 05 2021 Andreas Schneider <asn@redhat.com> - 1.17.0-1
- Initial package
