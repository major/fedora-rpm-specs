Name:           python-jupyter-builder
Version:        1.2.3
Release:        %autorelease
Summary:        Build tools for JupyterLab extensions
# jupyter-builder is BSD-3-Clause.
# Bundled node-semver is MIT.
# The rest are licenses of bundled JS libs.
#
# [[[cog
#    import cog
#    from glob import glob
#    from pathlib import Path
#    import json
#
#    file = sorted(
#        glob("python-jupyter-builder-*-build/jupyter_builder-*/THIRD_PARTY_LICENSES/yarn.js.third-party-licenses.json")
#        )[-1]
#    text = Path(file).read_text()
#    data = json.loads(text)
#    licenses = set([p["licenseId"] for p in data["packages"]])
#    for license in sorted(licenses):
#        cog.outl(f"# {license}")
# ]]]
# Apache-2.0
# BSD-2-Clause
# BSD-3-Clause
# ISC
# MIT
# [[[end]]]
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT
URL:            https://jupyter.org
Source:         %{pypi_source jupyter_builder}

BuildArch:      noarch
BuildRequires:  python3-devel
# For tests
BuildRequires:  toml-cli
BuildRequires:  python3dist(pytest)


%global _description %{expand:
Build tools for JupyterLab extensions — extracted from the core
JupyterLab codebase to be maintained and used independently.}

%description %_description

%package -n     python3-jupyter-builder
Summary:        %{summary}
# Bundled provides (uses data loaded above)
#
# [[[cog
#    packages = [(p["name"], p["versionInfo"]) for p in data["packages"]]
#    for name, version in sorted(packages):
#        cog.outl(f"Provides:       bundled(npm({name})) = {version}")
# ]]]
Provides:       bundled(npm(@arcanis/slice-ansi)) = 1.1.1
Provides:       bundled(npm(@chevrotain/utils)) = 9.1.0
Provides:       bundled(npm(@nodelib/fs.scandir)) = 2.1.5
Provides:       bundled(npm(@nodelib/fs.stat)) = 2.0.5
Provides:       bundled(npm(@nodelib/fs.walk)) = 1.2.7
Provides:       bundled(npm(@sindresorhus/is)) = 4.2.0
Provides:       bundled(npm(@szmarczak/http-timer)) = 4.0.5
Provides:       bundled(npm(@yarnpkg/cli)) = 3.5.0
Provides:       bundled(npm(@yarnpkg/core)) = 3.5.0
Provides:       bundled(npm(@yarnpkg/extensions)) = 1.1.2
Provides:       bundled(npm(@yarnpkg/fslib)) = 2.10.2
Provides:       bundled(npm(@yarnpkg/libzip)) = 2.3.0
Provides:       bundled(npm(@yarnpkg/nm)) = 3.1.0
Provides:       bundled(npm(@yarnpkg/parsers)) = 2.5.1
Provides:       bundled(npm(@yarnpkg/plugin-compat)) = 3.1.10
Provides:       bundled(npm(@yarnpkg/plugin-dlx)) = 3.1.4
Provides:       bundled(npm(@yarnpkg/plugin-essentials)) = 3.3.0
Provides:       bundled(npm(@yarnpkg/plugin-file)) = 2.3.1
Provides:       bundled(npm(@yarnpkg/plugin-git)) = 2.6.5
Provides:       bundled(npm(@yarnpkg/plugin-github)) = 2.3.1
Provides:       bundled(npm(@yarnpkg/plugin-http)) = 2.2.1
Provides:       bundled(npm(@yarnpkg/plugin-init)) = 3.2.1
Provides:       bundled(npm(@yarnpkg/plugin-link)) = 2.2.1
Provides:       bundled(npm(@yarnpkg/plugin-nm)) = 3.1.5
Provides:       bundled(npm(@yarnpkg/plugin-npm)) = 2.7.3
Provides:       bundled(npm(@yarnpkg/plugin-npm-cli)) = 3.3.0
Provides:       bundled(npm(@yarnpkg/plugin-pack)) = 3.2.0
Provides:       bundled(npm(@yarnpkg/plugin-patch)) = 3.2.4
Provides:       bundled(npm(@yarnpkg/plugin-pnp)) = 3.2.8
Provides:       bundled(npm(@yarnpkg/plugin-pnpm)) = 1.1.3
Provides:       bundled(npm(@yarnpkg/plugin-workspace-tools)) = 3.1.6
Provides:       bundled(npm(@yarnpkg/pnp)) = 3.3.1
Provides:       bundled(npm(@yarnpkg/shell)) = 3.2.5
Provides:       bundled(npm(@zkochan/cmd-shim)) = 5.1.0
Provides:       bundled(npm(ansi-colors)) = 4.1.1
Provides:       bundled(npm(ansi-regex)) = 5.0.1
Provides:       bundled(npm(ansi-styles)) = 4.2.0
Provides:       bundled(npm(arg)) = 5.0.2
Provides:       bundled(npm(array-union)) = 2.1.0
Provides:       bundled(npm(bl)) = 4.1.0
Provides:       bundled(npm(braces)) = 3.0.2
Provides:       bundled(npm(cacheable-lookup)) = 5.0.3
Provides:       bundled(npm(cacheable-request)) = 7.0.1
Provides:       bundled(npm(camelcase)) = 5.3.1
Provides:       bundled(npm(chalk)) = 3.0.0
Provides:       bundled(npm(chevrotain)) = 9.1.0
Provides:       bundled(npm(chownr)) = 2.0.0
Provides:       bundled(npm(ci-info)) = 3.2.0
Provides:       bundled(npm(clipanion)) = 3.2.0-rc.4
Provides:       bundled(npm(clone-response)) = 1.0.2
Provides:       bundled(npm(color-convert)) = 2.0.1
Provides:       bundled(npm(color-name)) = 1.1.4
Provides:       bundled(npm(cross-spawn)) = 7.0.3
Provides:       bundled(npm(decompress-response)) = 6.0.0
Provides:       bundled(npm(defer-to-connect)) = 2.0.0
Provides:       bundled(npm(diff)) = 5.1.0
Provides:       bundled(npm(dir-glob)) = 3.0.1
Provides:       bundled(npm(end-of-stream)) = 1.4.1
Provides:       bundled(npm(enquirer)) = 2.3.6
Provides:       bundled(npm(fast-glob)) = 3.2.2
Provides:       bundled(npm(fastq)) = 1.13.0
Provides:       bundled(npm(figgy-pudding)) = 3.5.1
Provides:       bundled(npm(fill-range)) = 7.0.1
Provides:       bundled(npm(fs-constants)) = 1.0.0
Provides:       bundled(npm(fs-minipass)) = 2.1.0
Provides:       bundled(npm(get-stream)) = 5.1.0
Provides:       bundled(npm(git-up)) = 7.0.0
Provides:       bundled(npm(git-url-parse)) = 13.1.0
Provides:       bundled(npm(glob-parent)) = 5.1.2
Provides:       bundled(npm(globby)) = 11.0.4
Provides:       bundled(npm(got)) = 11.8.2
Provides:       bundled(npm(grapheme-splitter)) = 1.0.4
Provides:       bundled(npm(has-flag)) = 4.0.0
Provides:       bundled(npm(http-cache-semantics)) = 4.1.0
Provides:       bundled(npm(http2-wrapper)) = 1.0.0-beta.5.2
Provides:       bundled(npm(ignore)) = 5.1.9
Provides:       bundled(npm(inherits)) = 2.0.4
Provides:       bundled(npm(is-extglob)) = 2.1.1
Provides:       bundled(npm(is-glob)) = 4.0.3
Provides:       bundled(npm(is-number)) = 7.0.0
Provides:       bundled(npm(is-ssh)) = 1.4.0
Provides:       bundled(npm(is-windows)) = 1.0.2
Provides:       bundled(npm(isexe)) = 2.0.0
Provides:       bundled(npm(js-yaml)) = 3.14.1
Provides:       bundled(npm(json-buffer)) = 3.0.1
Provides:       bundled(npm(keyv)) = 4.0.0
Provides:       bundled(npm(lodash)) = 4.17.21
Provides:       bundled(npm(lowercase-keys)) = 2.0.0
Provides:       bundled(npm(lru-cache)) = 6.0.0
Provides:       bundled(npm(merge2)) = 1.3.0
Provides:       bundled(npm(micromatch)) = 4.0.4
Provides:       bundled(npm(mimic-response)) = 1.0.1
Provides:       bundled(npm(mimic-response)) = 3.1.0
Provides:       bundled(npm(minipass)) = 3.3.5
Provides:       bundled(npm(minizlib)) = 2.1.2
Provides:       bundled(npm(mkdirp)) = 1.0.4
Provides:       bundled(npm(nanoclone)) = 0.2.1
Provides:       bundled(npm(normalize-url)) = 4.5.1
Provides:       bundled(npm(once)) = 1.4.0
Provides:       bundled(npm(p-cancelable)) = 2.0.0
Provides:       bundled(npm(p-limit)) = 2.2.0
Provides:       bundled(npm(p-try)) = 2.0.0
Provides:       bundled(npm(parse-path)) = 7.0.0
Provides:       bundled(npm(parse-url)) = 8.1.0
Provides:       bundled(npm(path-key)) = 3.1.1
Provides:       bundled(npm(path-type)) = 4.0.0
Provides:       bundled(npm(picomatch)) = 2.3.1
Provides:       bundled(npm(property-expr)) = 2.0.4
Provides:       bundled(npm(protocols)) = 2.0.1
Provides:       bundled(npm(pump)) = 3.0.0
Provides:       bundled(npm(quick-lru)) = 5.1.1
Provides:       bundled(npm(readable-stream)) = 3.6.0
Provides:       bundled(npm(regexp-to-ast)) = 0.5.0
Provides:       bundled(npm(resolve-alpn)) = 1.0.0
Provides:       bundled(npm(resolve.exports)) = 1.1.0
Provides:       bundled(npm(responselike)) = 2.0.0
Provides:       bundled(npm(reusify)) = 1.0.4
Provides:       bundled(npm(run-parallel)) = 1.1.9
Provides:       bundled(npm(safe-buffer)) = 5.1.2
Provides:       bundled(npm(semver)) = 7.3.5
Provides:       bundled(npm(shebang-command)) = 2.0.0
Provides:       bundled(npm(shebang-regex)) = 3.0.0
Provides:       bundled(npm(slash)) = 3.0.0
Provides:       bundled(npm(ssri)) = 6.0.1
Provides:       bundled(npm(string_decoder)) = 1.2.0
Provides:       bundled(npm(strip-ansi)) = 6.0.1
Provides:       bundled(npm(supports-color)) = 7.1.0
Provides:       bundled(npm(tar)) = 6.1.11
Provides:       bundled(npm(tar-stream)) = 2.2.0
Provides:       bundled(npm(tinylogic)) = 1.0.3
Provides:       bundled(npm(to-regex-range)) = 5.0.1
Provides:       bundled(npm(toposort)) = 2.0.2
Provides:       bundled(npm(treeify)) = 1.1.0
Provides:       bundled(npm(tunnel)) = 0.0.6
Provides:       bundled(npm(typanion)) = 3.3.2
Provides:       bundled(npm(util-deprecate)) = 1.0.2
Provides:       bundled(npm(which)) = 2.0.2
Provides:       bundled(npm(wrappy)) = 1.0.2
Provides:       bundled(npm(yallist)) = 4.0.0
Provides:       bundled(npm(yup)) = 0.32.9
# [[[end]]]


%description -n python3-jupyter-builder %_description


%prep
%autosetup -p1 -n jupyter_builder-%{version}

# Remove shebang line from yarn.js
sed -i '1{/^#!/d}' jupyter_builder/yarn.js

# Pytest cannot import copier
toml unset --toml-path pyproject.toml tool.pytest.ini_options.filterwarnings


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l jupyter_builder


%check
# Ignored tests require copier which is not packaged yet
%pytest --ignore tests/test_tpl.py


%files -n python3-jupyter-builder -f %{pyproject_files}
%doc README.md CHANGELOG.md
%{_bindir}/jupyter-builder
%{_bindir}/jlpm


%changelog
%autochangelog
