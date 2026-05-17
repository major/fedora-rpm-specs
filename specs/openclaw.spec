%global npm_name openclaw

Name:           openclaw
Version:        2026.5.7
Release:        %autorelease
Summary:        Your own personal AI assistant

License:        MIT AND (MIT AND Zlib) AND (MIT OR CC0-1.0) AND (MIT OR GPL-3.0-or-later) AND Apache-2.0 AND MPL-2.0 AND PSF-2.0 AND 0BSD AND BSD-2-Clause AND BSD-3-Clause AND ISC AND BlueOak-1.0.0 AND CC-BY-SA-4.0 AND CC0-1.0
# see license-checker.txt for a breakdown
# Some oddballs from the licensecheck.txt
#
# *No copyright* GNU General Public License
# -----------------------------------------
# openclaw-2026.5.4-build/package/node_modules_prod/argparse/LICENSE
#
# argparse is listed as Python-2.0
# The LICENSE file goes into a lot of history of what license for what historic python
# GPL is mentioned only within the context of is this file and any time compatible
# with GPL. The main project listing of Python-2.0 is consistent with this file
# Python-2.0 short SPDX form is PSF-2.0
#
# *No copyright* X11 License
# --------------------------
# openclaw-2026.5.4-build/package/node_modules_prod/jszip/vendor/FileSaver.js
# jszip is listed as (MIT OR GPL-3.0-or-later)
# This is the line
#  *  License: X11/MIT
# This is consistent with MIT
#
# BSD 2-Clause with views sentence
# --------------------------------
# openclaw-2026.5.4-build/package/node_modules_prod/fast-uri/test/uri-js.test.js
# fast-uri is listed as BSD-3-Clause
# This file has a BSD-2-Clause license.  The 'views sentence' refers to this part
# at the end
#    * The views and conclusions contained in the software ...
# and does not pertain to licenses.
#
# SIL Open Font License 1.1
# -------------------------
# openclaw-2026.5.4-build/package/node_modules_prod/pdfjs-dist/standard_fonts/LICENSE_LIBERATION
# pdfjs-dist is listed as Apache-2.0
# See the 'removing fonts' in the prep section
# No fonts remaining.

URL:            https://github.com/openclaw/openclaw
Source0:        https://registry.npmjs.org/openclaw/-/openclaw-%{version}.tgz
# nodejs-packaging-bundler openclaw <version>
# problems with dev dependencies
#  Downloading dev dependencies
#  npm error code EUNSUPPORTEDPROTOCOL
#  npm error Unsupported URL Type "workspace:": workspace:*
Source1:        %{npm_name}-%{version}-nm-prod.tgz
Source2:        %{npm_name}-%{version}-bundled-licenses.txt
# npn i -g license-checker
# (in installed rpm dir run) license-checker 
Source10:       license-checker.txt

BuildArch:      noarch
ExclusiveArch:  x86_64 aarch64

BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  nodejs-devel

Requires:       nodejs

%description
OpenClaw is a personal AI assistant you run on your own devices. It answers
you on the channels you already use. 

If you want a personal, single-user assistant that feels local, fast,
and always-on, this is it.

%prep
%setup -q -n package

cp -p %{SOURCE2} %{npm_name}-%{version}-bundled-licenses.txt

# Some adjustments to the nodejs-packaging-bundler
# There are two Apache license
# "Apache 2.0"
# "Apache-2.0"
# The correct form is Apache-2.0, remove the first
sed -i '/Apache 2.0/d' %{npm_name}-%{version}-bundled-licenses.txt

tar xfz %{SOURCE1}
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
ln -s ../node_modules_prod/.bin .
popd

# remove zero length files
find . -size 0 -type f -print0 | xargs -0 rm -f

# remove hidden things
N=".babelrc.es5 .babelrc.lib .bin .boundary-entry-shims.stamp .claude .codeclimate.yml \
   .editorconfig .env .env.example .eslintrc .eslintrc.cjs .eslintrc.js .eslintrc.json .eslintrc.yml .eslintignore \
   .gitattributes .github .gitkeep .history .i18n .keep .jscs.json .jshintrc .jekyll-metadata .npmignore .nvmrc .nycrc \
   .package-lock.json .prettierignore .prettierrc .prettierrc.js .prettierrc.json .prettierrc.yaml .runkit_example.js .travis.yml"
for n in $N; do
    find . -name ${n} -print0 | xargs -0 rm -rf
done

# remove devel things
find . -name '*.h' -type f -print0 | xargs -0 rm -rf
find . -name '*.c' -type f -print0 | xargs -0 rm -rf
find . -name '*.so' -type f -print0 | xargs -0 rm -rf

# remove fonts
find . -name '*.ttf' -type f -print0 | xargs -0 rm -rf

# remove arch things
N="linux-arm64 linux-x64 darwin-arm64 darwin-x64 win32-arm64 win32-x86"
for n in $N; do
    find . -name ${n} -print0 | xargs -0 rm -rf
done

# make some scripts executable
N="dist/extensions/lmstudio/node_modules_prod/@mariozechner/pi-ai/dist/cli.d.ts
node_modules_prod/@agentclientprotocol/sdk/dist/examples/agent.d.ts
node_modules_prod/@agentclientprotocol/sdk/dist/examples/agent.js
node_modules_prod/@agentclientprotocol/sdk/dist/examples/client.d.ts
node_modules_prod/@agentclientprotocol/sdk/dist/examples/client.js
node_modules_prod/@mariozechner/pi-ai/dist/cli.d.ts
node_modules_prod/@mariozechner/pi-coding-agent/dist/bun/cli.d.ts
node_modules_prod/@mariozechner/pi-coding-agent/dist/bun/cli.js
node_modules_prod/@mariozechner/pi-coding-agent/dist/cli.d.ts
node_modules_prod/@modelcontextprotocol/sdk/dist/cjs/examples/client/simpleClientCredentials.d.ts
node_modules_prod/@modelcontextprotocol/sdk/dist/cjs/examples/client/simpleClientCredentials.js
node_modules_prod/@modelcontextprotocol/sdk/dist/cjs/examples/client/simpleOAuthClient.d.ts
node_modules_prod/@modelcontextprotocol/sdk/dist/cjs/examples/client/simpleOAuthClient.js
node_modules_prod/@modelcontextprotocol/sdk/dist/cjs/examples/server/mcpServerOutputSchema.d.ts
node_modules_prod/@modelcontextprotocol/sdk/dist/cjs/examples/server/mcpServerOutputSchema.js
node_modules_prod/@modelcontextprotocol/sdk/dist/esm/examples/client/simpleClientCredentials.d.ts
node_modules_prod/@modelcontextprotocol/sdk/dist/esm/examples/client/simpleClientCredentials.js
node_modules_prod/@modelcontextprotocol/sdk/dist/esm/examples/client/simpleOAuthClient.d.ts
node_modules_prod/@modelcontextprotocol/sdk/dist/esm/examples/client/simpleOAuthClient.js
node_modules_prod/@modelcontextprotocol/sdk/dist/esm/examples/server/mcpServerOutputSchema.d.ts
node_modules_prod/@modelcontextprotocol/sdk/dist/esm/examples/server/mcpServerOutputSchema.js
node_modules_prod/marked/bin/main.js
node_modules_prod/node-addon-api/tools/clang-format.js
node_modules_prod/tokenjuice/dist/cli/main.d.ts
scripts/postinstall-bundled-plugins.mjs
skills/model-usage/scripts/model_usage.py
skills/model-usage/scripts/test_model_usage.py
skills/openai-whisper-api/scripts/transcribe.sh
skills/skill-creator/scripts/init_skill.py
skills/skill-creator/scripts/package_skill.py
skills/skill-creator/scripts/quick_validate.py
skills/skill-creator/scripts/test_package_skill.py
skills/skill-creator/scripts/test_quick_validate.py
skills/video-frames/scripts/frame.sh"
for n in $N; do
    chmod a+x ${n}
done

# remove some execute permisions
N="dist/extensions/lmstudio/node_modules_prod/@aws-sdk/types/package.json
node_modules_prod/@aws-sdk/types/package.json
node_modules_prod/sisteransi/package.json"
for n in $N; do
    chmod a-x ${n}
done

# fix line endings
dos2unix node_modules_prod/node-edge-tts/bin.js

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr * %{buildroot}%{nodejs_sitelib}/%{npm_name}/

mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -s ../lib/node_modules/%{npm_name}/openclaw.mjs openclaw
popd

# cleanup dupes
%fdupes %{buildroot}

%files
%license LICENSE %{npm_name}-%{version}-bundled-licenses.txt
%doc README.md
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/openclaw

%changelog
%autochangelog
