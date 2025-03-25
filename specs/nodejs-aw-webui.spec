%global npm_name aw-webui

%global commit cb9a7ecc58de8f4ffcc674deb44a52e10b2c6225
%global short_commit %(c=%{commit}; echo ${c:0:7})

Name:           nodejs-%{npm_name}
Version:        0^20250323.%{short_commit}
Release:        %autorelease
Summary:        A web-based UI for ActivityWatch, built with Vue.js

# The aw-webui is released under the MPL-2.0 license. Other licenses:
# src/visualizations/sunburst-clock.ts: Apache-2.0
# src/visualizations/ForceGraph.vue: ISC
License:        MPL-2.0 AND Apache-2.0 AND ISC

URL:            https://github.com/ActivityWatch/%{npm_name}
Source0:        %{url}/archive/%{commit}/%{npm_name}-%{short_commit}.tar.gz
# prepared with "nodejs-packaging-bundler %%{npm_name} %%{short_commit} %%{SOURCE0}"
Source1:        %{npm_name}-%{short_commit}-nm-prod.tgz
Source2:        %{npm_name}-%{short_commit}-nm-dev.tgz
Source3:        %{npm_name}-%{short_commit}-bundled-licenses.txt
Source4:        https://raw.githubusercontent.com/ActivityWatch/media/cb597f7c2e2b135505fe5d6b3042960a638892cf/logo/logo.png
Source5:        https://raw.githubusercontent.com/ActivityWatch/media/cb597f7c2e2b135505fe5d6b3042960a638892cf/logo/logo.svg

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch
BuildRequires:  nodejs-npm
BuildRequires:  nodejs-devel
BuildRequires:  fdupes

%description
%{summary}

%prep
%autosetup -n %{npm_name}-%{commit} -p1

# copy license
cp -p %{SOURCE3} .

# copy icons
cp -p %{SOURCE4} %{SOURCE5} -t static

# it's not a git repository, so querying git would fail
sed -ri 's/git rev-parse --short HEAD/echo %{short_commit}/' vue.config.js

sed -ri '/typeface-varela-round/d'  src/main.js

# unpack npm prod dependencies straight to node_modules, because
# building fails when symlinking from node_modules_prod to node_modules
mkdir -p node_modules
tar xfz %{SOURCE1} --strip-components 2 -C node_modules

# unpack npm dev dependencies too, because cannot find vue-cli-service
# when building
tar xfz %{SOURCE2} --strip-components 2 -C node_modules

%build
npm run build

%install
mkdir -p %{buildroot}%{_datadir}/%{npm_name}
cp -pr dist -t %{buildroot}%{_datadir}/%{npm_name}

%fdupes %{buildroot}%{_datadir}/%{npm_name}/dist/css

%check
npm test

%files
%license LICENSE.txt %{npm_name}-%{short_commit}-bundled-licenses.txt
%doc README.md
%{_datadir}/%{npm_name}

%changelog
%autochangelog
