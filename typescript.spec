Name:           typescript
Version:        4.8.4
Release:        %autorelease
Summary:        A language for application scale JavaScript development
License:        Apache-2.0
URL:            https://www.typescriptlang.org
Source:         https://registry.npmjs.org/typescript/-/typescript-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs
BuildRequires:  nodejs-packaging
# Obsoletes added in F38, can be removed in F40.
Provides:       nodejs-typescript = %{version}-%{release}
Obsoletes:      nodejs-typescript < 4.1.3-6


%description
TypeScript is a language for application-scale JavaScript. TypeScript adds
optional types to JavaScript that support tools for large-scale JavaScript
applications for any browser, for any host, on any OS. TypeScript compiles to
readable, standards-based JavaScript.


%prep
%autosetup -n package


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/typescript
cp -pr package.json bin/ lib/ %{buildroot}%{nodejs_sitelib}/typescript

mkdir -p %{buildroot}%{_bindir}
ln -s ../lib/node_modules/typescript/bin/tsc %{buildroot}%{_bindir}/tsc
ln -s ../lib/node_modules/typescript/bin/tsserver %{buildroot}%{_bindir}/tsserver


%check
%{__nodejs} -e 'require("./")'


%files
%license LICENSE.txt CopyrightNotice.txt
%{nodejs_sitelib}/typescript
%{_bindir}/tsc
%{_bindir}/tsserver


%changelog
%autochangelog
