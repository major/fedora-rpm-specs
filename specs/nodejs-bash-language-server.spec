%{?nodejs_default_filter}

%define pkg_name bash-language-server

Name:           nodejs-bash-language-server
Version:        5.4.3
Release:        %autorelease
Summary:        A language server for Bash
License:        MIT
Url:            https://github.com/bash-lsp/bash-language-server
Source0:        %{url}/archive/server-%{version}/%{pkg_name}-%{version}.tar.gz
# Create with `bash prepare_vendor.sh`
Source1:        %{pkg_name}-%{version}-vendor.tar.zst
# Create with: nodejs-packaging-bundler bash-language-server 5.1.1
Source2:        bash-language-server-bundled-licenses.txt
BuildRequires:  fdupes
BuildRequires:  npm(typescript)
BuildRequires:  nodejs-packaging
BuildRequires:  nodejs-npm
BuildRequires:  perl-interpreter
BuildRequires:  pnpm
BuildArch:      noarch
ExclusiveArch: %{nodejs_arches} noarch
Recommends:     ShellCheck

%description
Bash language server implementation based on Tree Sitter and its grammar for
Bash with explainshell integration.

%prep
%autosetup -n %{pkg_name}-server-%{version} -a1 -p1

cp %{SOURCE2} .

%build
pnpm install --offline --frozen-lockfile --store-dir="$(pwd)/.pnpm-store"

npm run compile

%install
# Only install production dependencies in node_modules
rm -rf node_modules/
pnpm install --production --offline --frozen-lockfile --package-import-method copy --store-dir="$(pwd)/.pnpm-store"

for S in $(grep -l '#!.*node' \
    server/out/cli.js \
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

install -d -m 0755 %{buildroot}%{nodejs_sitelib}/%{pkg_name}/

cp -av server %{buildroot}%{nodejs_sitelib}/%{pkg_name}/
cp -av node_modules %{buildroot}%{nodejs_sitelib}/%{pkg_name}/

install -d -m 0755 %{buildroot}%{_bindir}
cat << EOF > %{buildroot}%{_bindir}/%{pkg_name}
#!/bin/sh
export NODE_ENV=production

exec /usr/bin/node %{nodejs_sitelib}/%{pkg_name}/server/out/cli.js "\$@"
EOF
chmod +x %{buildroot}%{_bindir}/%{pkg_name}

find %{buildroot}%{nodejs_sitelib}/%{pkg_name} -name "*.bak" -delete
find %{buildroot}%{nodejs_sitelib}/%{pkg_name} -type f -name "\.*" -delete
find %{buildroot}%{nodejs_sitelib}/%{pkg_name} -type d -name "\.bin" -print0 | xargs -0 rm -rf
find %{buildroot}%{nodejs_sitelib}/%{pkg_name} -type d -name "\.github" -print0 | xargs -0 rm -rf

rm -rf %{buildroot}%{nodejs_sitelib}/%{pkg_name}/server/node_modules/ajv/scripts/
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkg_name}/server/node_modules/dashdash/etc/
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkg_name}/server/node_modules/performance-now/test/

rm %{buildroot}%{nodejs_sitelib}/%{pkg_name}/server/src/get-options.sh

# dangling symlinks
rm %{buildroot}%{nodejs_sitelib}/%{pkg_name}/server/node_modules/@types/fuzzy-search
rm %{buildroot}%{nodejs_sitelib}/%{pkg_name}/server/node_modules/@types/node-fetch
rm %{buildroot}%{nodejs_sitelib}/%{pkg_name}/server/node_modules/@types/turndown
rm %{buildroot}%{nodejs_sitelib}/%{pkg_name}/server/node_modules/@types/urijs

%fdupes %{buildroot}%{nodejs_sitelib}/%{pkg_name}

%files
%license LICENSE bash-language-server-bundled-licenses.txt
%doc README.md
%{_bindir}/%{pkg_name}
%{nodejs_sitelib}/%{pkg_name}/

%changelog
%autochangelog
