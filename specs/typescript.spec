Name:           typescript
Version:        5.7.3
Release:        %autorelease
Summary:        A language for application-scale JavaScript
License:        Apache-2.0
URL:            https://www.typescriptlang.org
Source:         https://registry.npmjs.org/typescript/-/typescript-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-devel


%description
TypeScript is a language for application-scale JavaScript. TypeScript adds
optional types to JavaScript that support tools for large-scale JavaScript
applications for any browser, for any host, on any OS. TypeScript compiles to
readable, standards-based JavaScript.


%prep
%autosetup -n package
# adjust the shebang lines to get a runtime dependency matching the
# node_modules_* directory where the code is actually installed to
sed -e '/#!/ s/node/node-%{_nodejs_major_version}/' -i bin/tsc bin/tsserver


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/typescript
cp -pr package.json bin/ lib/ %{buildroot}%{nodejs_sitelib}/typescript

mkdir -p %{buildroot}%{_bindir}
# this symlink must use the major version path or else it will break after a
# nodejs major version bump
ln -s ../lib/node_modules_%{_nodejs_major_version}/typescript/bin/tsc %{buildroot}%{_bindir}/tsc
ln -s ../lib/node_modules_%{_nodejs_major_version}/typescript/bin/tsserver %{buildroot}%{_bindir}/tsserver


%check
%{__nodejs} -e 'require("./")'


%files
%license LICENSE.txt
%{nodejs_sitelib}/typescript
%{_bindir}/tsc
%{_bindir}/tsserver


%changelog
%autochangelog
