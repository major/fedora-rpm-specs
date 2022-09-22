%{?nodejs_find_provides_and_requires}

%global npm_name less

Name:           nodejs-%{npm_name}
Version:        4.1.2
Release:        %autorelease
Summary:        Less.js The dynamic stylesheet language

# cssmin.js is licensed under BSD license
# everything else is ASL 2.0
License:        ASL 2.0 and BSD

URL:            http://lesscss.org
Source0: http://registry.npmjs.org/less/-/less-%{version}.tgz
Source1: %{npm_name}-%{version}-nm-prod.tgz

BuildArch:      noarch
BuildRequires:  nodejs-devel
BuildRequires:  nodejs-packaging
Requires:       nodejs
ExclusiveArch: %{nodejs_arches} noarch

Provides:  lessjs = %{version}-%{release}
Obsoletes: lessjs < 1.3.3-2


%description
LESS extends CSS with dynamic behavior such as variables, mixins, operations
and functions. LESS runs on both the client-side (Chrome, Safari, Firefox)
and server-side, with Node.js and Rhino.


%prep
%autosetup -n package -p1

# Remove pre-built files from the dist/ directory
rm -f dist/*.js

tar xfz %{SOURCE1}
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
ln -s ../node_modules_prod/.bin .
popd


%build
# Nothing to be built, we're just carrying around flat files


%check
pushd %{buildroot}%{nodejs_sitelib}/%{npm_name}
%{__nodejs} -e 'require("./")'
popd


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/less

cp -rp index.js \
       package.json \
       lib/ \
       %{buildroot}/%{nodejs_sitelib}/less

# Copy over bundled nodejs modules
cp -pr node_modules node_modules_prod \
    %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{nodejs_sitelib}/less/bin
install -p -D -m0755 bin/lessc %{buildroot}%{nodejs_sitelib}/less/bin/lessc

# Install /usr/bin/lessc
mkdir -p %{buildroot}%{_bindir}
ln -srf %{buildroot}%{nodejs_sitelib}/less/bin/lessc \
        %{buildroot}%{_bindir}


%files
%doc README.md
%{_bindir}/lessc
%{nodejs_sitelib}/less


%changelog
%autochangelog
