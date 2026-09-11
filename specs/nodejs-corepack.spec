%global npm_name corepack

Name:           nodejs-%{npm_name}
Version:        0.36.0
Release:        %autorelease
Summary:        Package manager version manager for Node.js projects

License:        MIT
URL:            https://github.com/nodejs/corepack
Source0:        https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

Requires:       nodejs
BuildRequires:  nodejs-devel
BuildRequires:  npm

%description
Corepack is a zero-runtime-dependency Node.js script that acts as a
bridge between Node.js projects and the package managers they are
intended to be used with during development. In practical terms,
Corepack lets you use Yarn, npm, and pnpm without having to install
them.


%prep
%autosetup -n package -p1


%build
# nothing to do


%install
export npm_config_prefix=%{buildroot}%{_prefix}
npm install --global --install-links .


%check
%{buildroot}/%{_bindir}/corepack --version


%files
%license LICENSE.md
%doc CHANGELOG.md README.md
%{_bindir}/corepack
%ghost %{_bindir}/pnpm
%ghost %{_bindir}/pnpx
%ghost %{_bindir}/yarn
%ghost %{_bindir}/yarnpkg
%{nodejs_sitearch}/corepack
%exclude %{nodejs_sitearch}/corepack/shims/nodewin/*.cmd
%exclude %{nodejs_sitearch}/corepack/shims/nodewin/*.ps1
%exclude %{nodejs_sitearch}/corepack/shims/*.cmd
%exclude %{nodejs_sitearch}/corepack/shims/*.ps1


%changelog
%{autochangelog}
