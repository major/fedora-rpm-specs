%global npm_name @earendil-works/pi-coding-agent

Name:           pi-coding-agent
Version:        0.80.3
Release:        %autorelease
Summary:        An open source coding agent

License:        MIT AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND BlueOak-1.0.0 AND 0BSD AND CC-BY-SA-4.0 AND CC0-1.0
# To add a LICENSE file to the project
# https://github.com/badlogic/pi-mono/issues/4215
# MIT is mentioned in the README.md
#
# see license-checker.txt for a breakdown of the depend projects
URL:            https://github.com/earendil-works/pi
# npm pack @earendil-works/pi-coding-agent
Source0:        earendil-works-pi-coding-agent-%{version}.tgz
# nodejs-packaging-bundler @earendil-works/pi-coding-agent <version>
Source1:        @earendil-works-pi-coding-agent-%{version}-nm-prod.tgz
Source2:        @earendil-works-pi-coding-agent-%{version}-bundled-licenses.txt

# npm i -g license-checker
# (in installed rpm dir run) license-checker 
Source10:       license-checker.txt

BuildArch:      noarch
ExclusiveArch:  x86_64 aarch64

Requires:       nodejs
BuildRequires:  nodejs-devel
BuildRequires:  fdupes

%description
Pi is a minimal terminal coding harness. Adapt pi to your workflows,
not the other way around, without having to fork and modify pi internals.
Extend it with TypeScript Extensions, Skills, Prompt Templates, and
Themes. Put your extensions, skills, prompt templates, and themes in Pi
Packages and share them with others via npm or git.

Pi ships with powerful defaults but skips features like sub agents and
plan mode. Instead, you can ask pi to build what you want or install a
third party pi package that matches your workflow.

Pi runs in four modes: interactive, print or JSON, RPC for process
integration, and an SDK for embedding in your own apps.
See openclaw/openclaw for a real-world SDK integration.

%prep
%setup -q -n package

cp -p %{SOURCE2} %{name}-%{version}-bundled-licenses.txt

tar xfz %{SOURCE1}
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
ln -s ../node_modules_prod/.bin .
popd

# Strip out examples
rm -rf examples

# remove zero length files
find . -size 0 -type f -print0 | xargs -0 rm -f

# remove hidden things
# pi-coding-agent.noarch: W: hidden-file-or-dir /usr/lib/node_modules/
#  @mariozechner/pi-coding-agent/node_modules_prod/socks/.eslintrc.cjs
N=".bin .claude .editorconfig .eslintrc .eslintrc.cjs .eslintrc.js .eslintignore .github \
   .gitkeep .history .keep .jscs.json .jshintrc .npmignore .nvmrc \
   .package-lock.json .prettierignore .prettierrc .prettierrc.json .prettierrc.yaml .travis.yml"
for n in $N; do
    find . -name ${n} -print0 | xargs -0 rm -rf
done

# remove devel things
# pi-coding-agent.noarch: W: devel-file-in-non-devel-package /usr/lib/node_modules/
#   @mariozechner/pi-coding-agent/node_modules_prod/@tootallnate/quickjs-emscripten/c/interface.c
find . -name 'interface.c' -print0 | xargs -0 rm -rf

# remove some binaries
rm -rf node_modules_prod/@earendil-works/pi-tui/native
rm -f node_modules_prod/@silvia-odwyer/photon-node/photon_rs_bg.wasm

# make some scripts executable
chmod a+x dist/bun/cli.d.ts
chmod a+x dist/bun/cli.js
chmod a+x dist/cli.d.ts
chmod a+x dist/rpc-entry.d.ts
chmod a+x node_modules_prod/@earendil-works/pi-ai/dist/cli.d.ts
chmod a+x node_modules_prod/marked/bin/main.js

# remove some execute permisions
chmod a-x node_modules_prod/@aws-sdk/types/package.json

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr * %{buildroot}%{nodejs_sitelib}/%{npm_name}/

mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -s ../lib/node_modules/%{npm_name}/dist/cli.js pi
popd

# cleanup dupes
%fdupes %{buildroot}

%files
%license README.md %{name}-%{version}-bundled-licenses.txt
%doc README.md
%dir %{nodejs_sitelib}/@earendil-works
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/pi

%changelog
%autochangelog
