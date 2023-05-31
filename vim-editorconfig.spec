# Currently, rubygem(vimrunner) is not packaged so we cannot run the plugin
# tests. Some other work may be required to get them running. See also
# https://github.com/editorconfig/editorconfig-vim/issues/150.
%bcond_with plugin_tests

# In Fedora, vim plugin packages should ideally start with the vim- prefix:
Name:           vim-editorconfig
Summary:        EditorConfig Vim Plugin
Version:        1.1.1
Release:        %autorelease

# The editorconfig core tests are included as a git submodule do not appear in
# the GitHub-generated release tarball, so we need a separate source archive
# for them.  We do not treat this as a bundled library because the tests do not
# contribute to the installed files in any way. When the package is updated,
# the maintainer should check that we still have the correct (latest) version
# of the tests.
%global core_tests_version 0.13
%global core_tests_url https://github.com/editorconfig/editorconfig-core-test/
# Same for the plugin tests; these do not tag releases, so we reference a
# particular commit.
%global plugin_tests_commit cb7ae15d16ab3d72a1139f7a629b11cfe16d972f
%global plugin_tests_url https://github.com/editorconfig/editorconfig-plugin-tests/

# The entire source is BSD-2-Clause, except that the following files are
# (BSD-2-Clause AND PSF-2.0) since they are derived from the Python standard
# library:
#   - autoload/editorconfig_core/fnmatch.vim
#   - autoload/editorconfig_core/ini.vim
License:        BSD-2-Clause AND (BSD-2-Clause AND PSF-2.0)
URL:            https://github.com/editorconfig/editorconfig-vim
Source0:        %{url}/archive/v%{version}/editorconfig-vim-%{version}.tar.gz
Source1:        %{core_tests_url}/archive/v%{core_tests_version}/editorconfig-core-test-%{core_tests_version}.tar.gz
# Files in this source are licensed CC-BY; however, nothing derived from them
# is installed, so this does not affect the License field.
Source2:        %{plugin_tests_url}/archive/%{plugin_tests_commit}/editorconfig-plugin-tests-%{plugin_tests_commit}.tar.gz

BuildArch:      noarch

# For all tests:
BuildRequires:  editorconfig
BuildRequires:  vim-enhanced
# For core tests
BuildRequires:  cmake
%if %{with plugin_tests}
# For plugin tests
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  rubygem(rake)
BuildRequires:  rubygem(rspec)
# tests/plugin/spec/editorconfig_spec.rb: require 'vimrunner'
BuildRequires:  rubygem(vimrunner)
%endif

Requires:       vim-filesystem
# The plugin calls the editorconfig executable.
Requires:       editorconfig

%description
This is an EditorConfig plugin for Vim.


%prep
%autosetup -n editorconfig-vim-%{version}

# Copy in the editorconfig core and plugin tests from the respective GitHub
# tarballs.
rm -rvf tests/core/tests
%setup -q -T -D -b 1 -n editorconfig-vim-%{version}
cp -rp ../editorconfig-core-test-%{core_tests_version} tests/core/tests
%if %{with plugin_tests}
rm -rvf tests/plugin/spec/plugin_tests
%setup -q -T -D -b 2 -n editorconfig-vim-%{version}
cp -rp ../editorconfig-plugin-tests-%{plugin_tests_commit} \
    tests/plugin/spec/plugin_tests
%endif

# Fix executable bit on license file
chmod -v a-x LICENSE.PSF


%build
pushd tests/core
%cmake
# There is not actually anything to do here:
%cmake_build
popd


%install
install -d '%{buildroot}%{_datadir}/vim/vimfiles'
cp -rvp autoload plugin '%{buildroot}%{_datadir}/vim/vimfiles'


%check
# Core tests: these could also be executed by “./tests/travis-test.sh core”.
pushd tests/core
%ctest
popd

%if %{with plugin_tests}
# Plugin tests:
export EDITORCONFIG_VIM_EXTERNAL_CORE='%{_bindir}/editorconfig'
%{_bindir}/xvfb-run -a rspec tests/plugin/spec/editorconfig_spec.rb
%endif


%files
%license LICENSE LICENSE.PSF
%doc CONTRIBUTORS
%doc README.md
%doc doc/*.txt

%{_datadir}/vim/vimfiles/autoload/editorconfig.vim
%{_datadir}/vim/vimfiles/autoload/editorconfig_core.vim
%{_datadir}/vim/vimfiles/autoload/editorconfig_core
%{_datadir}/vim/vimfiles/plugin/editorconfig.vim


%changelog
%autochangelog
