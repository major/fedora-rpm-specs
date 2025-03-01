Name:           httpie
Version:        3.2.4
Release:        %autorelease
Summary:        A Curl-like tool for humans

License:        BSD-3-Clause
URL:            https://httpie.org/
Source:         https://github.com/httpie/cli/archive/%{version}/cli-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

# The tests are enabled by default, --without tests option exists
%bcond_without tests

%description
HTTPie is a CLI HTTP utility built out of frustration with existing tools. The
goal is to make CLI interaction with HTTP-based services as human-friendly as
possible.

HTTPie does so by providing an http command that allows for issuing arbitrary
HTTP requests using a simple and natural syntax and displaying colorized
responses.


%prep
%autosetup -p1 -n cli-%{version}

# Upstream pins werkzeug<2.1.0 to avoid a problem in httpbin that Fedora has patch for
# https://github.com/httpie/httpie/pull/1345
# we revert it to allow building with newer werkzeug
sed -i "/werkzeug<2.1.0/d" setup.cfg


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x test}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files httpie

# Bash completion
mkdir -p %{buildroot}%{bash_completions_dir}
cp -a extras/httpie-completion.bash %{buildroot}%{bash_completions_dir}/http
ln -s ./http %{buildroot}%{bash_completions_dir}/https

# Fish completion
mkdir -p %{buildroot}%{fish_completions_dir}/
cp -a extras/httpie-completion.fish %{buildroot}%{fish_completions_dir}/http.fish
ln -s ./http.fish %{buildroot}%{fish_completions_dir}/https.fish

# Man pages
mkdir -p %{buildroot}%{_mandir}/man1
cp -a extras/man/*.1 %{buildroot}%{_mandir}/man1/


%check
%if %{with tests}
# Werkzeug >= 3 failures
# https://github.com/httpie/cli/issues/1530
issue1530="not test_compress_form and not test_binary"
# Disabled plugins tests, TODO investigate
plugins="not test_plugins_installation and not test_plugin_installation_with_custom_config and not test_plugins_listing and not test_plugins_uninstall and not test_plugins_double_uninstall and not test_broken_plugins"
# New argparse behavior, TODO report upstream
argparse="not (test_naked_invocation and args3)"
%pytest -v -k "$issue1530 and $plugins and $argparse"
%else
%pyproject_check_import
%endif


%files -f %{pyproject_files}
%doc README.md
%{_bindir}/http
%{_bindir}/https
%{_bindir}/httpie
%{_mandir}/man1/http.1*
%{_mandir}/man1/https.1*
%{_mandir}/man1/httpie.1*
%{bash_completions_dir}/http
%{bash_completions_dir}/https
%{fish_completions_dir}/http.fish
%{fish_completions_dir}/https.fish


%changelog
%autochangelog
