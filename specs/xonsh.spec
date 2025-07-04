Name:           xonsh
Version:        0.19.9
Release:        %autorelease
Summary:        A general purpose, Python-ish shell

# xonsh is BSD-2-Clause.
# xonsh/winutils.py and xonsh/xoreutils/_which.py contain MIT code.
License:        BSD-2-Clause AND MIT
URL:            https://xon.sh
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
# needed for tests:
BuildRequires:  %{py3_dist ply}
BuildRequires:  %{py3_dist prompt-toolkit}
BuildRequires:  %{py3_dist pygments}
BuildRequires:  %{py3_dist pyte}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-mock}
BuildRequires:  %{py3_dist pytest-subprocess}
BuildRequires:  %{py3_dist pytest-rerunfailures}
BuildRequires:  %{py3_dist requests}
BuildRequires:  %{py3_dist virtualenv}
BuildRequires:  bash-completion
BuildRequires:  git-core
BuildRequires:  man-db
BuildRequires:  /usr/bin/python

# required by "ptk" extra:
Requires:       %{py3_dist prompt-toolkit}
Requires:       %{py3_dist pygments}
Requires:       %{py3_dist pyperclip}

# required by "setproctitle" extra:
Requires:       %{py3_dist setproctitle}

# required by "full" extra:
Requires:       %{py3_dist distro}
Requires:       %{py3_dist ujson}

# unbundled in prep
Requires:       %{py3_dist ply}

# required for vox
Requires:       %{py3_dist virtualenv}

Recommends:     bash-completion

%description
xonsh is a Python-powered, cross-platform, Unix-gazing shell language and
command prompt.

The language is a superset of Python 3.6+ with additional shell primitives.
xonsh (pronounced conch) is meant for the daily use of experts and novices
alike.

%prep
%autosetup -p1 -n %{name}-%{version}

# Unbundle ply
sed --in-place '/xonsh\.parsers\.ply/d' pyproject.toml
sed --in-place -e 's/xonsh\.parsers\.ply/ply/' \
               -e 's/from xonsh\.parsers import ply/import ply/' \
               $(grep -Erl --include='*.py' 'xonsh\.parsers( import |\.)ply')
rm -r xonsh/parsers/ply

# Remove shebang.
sed --in-place "s:#!\s*/usr.*::" xonsh/xoreutils/_which.py xonsh/webconfig/main.py

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files xompletions xonsh xontrib

%check
# Altering PYTHONPATH makes the tests importable.
%global __pytest PYTHONPATH="$PYTHONPATH:$(pwd)" %{python3} -m xonsh run-tests.xsh test --
# TODO: broken tests
# deselected test_integrations fail due to unexpected DeprecationWarning in output, setting PYTHONWARNINGS does not help
#pytest -v -k "not test_is_tok_color_dict and not test_ptk_prompt and not test_vc_get_branch[hg] and not test_vc_get_branch[fossil] and not test_callable_alias_no_bad_file_descriptor and not test_dirty_working_directory[hg]"
%pytest -v || :

%post
if [ "$1" -ge 1 ]; then
  if [ ! -f %{_sysconfdir}/shells ] ; then
    touch %{_sysconfdir}/shells
  fi
  for binpath in %{_bindir} /bin; do
    if ! grep -q "^${binpath}/xonsh$" %{_sysconfdir}/shells; then
       (cat %{_sysconfdir}/shells; echo "$binpath/xonsh") > %{_sysconfdir}/shells.new
       mv %{_sysconfdir}/shells{.new,}
    fi
  done
fi

%postun
if [ "$1" = 0 ] && [ -f %{_sysconfdir}/shells ] ; then
  sed -e '\!^%{_bindir}/xonsh$!d' -e '\!^/bin/xonsh$!d' < %{_sysconfdir}/shells > %{_sysconfdir}/shells.new
  mv %{_sysconfdir}/shells{.new,}
fi

%files -f %{pyproject_files}
%doc README.rst
%license license
%{_bindir}/xonsh
%{_bindir}/xonsh-cat
%{_bindir}/xonsh-uname
%{_bindir}/xonsh-uptime

%changelog
%autochangelog
