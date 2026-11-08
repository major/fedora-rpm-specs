%global pypi_name shtab

Name:           python-shtab
Version:        1.13.0
Release:        %autorelease
Summary:        Automagic shell tab completion for Python CLI applications

License:        Apache-2.0
URL:            https://github.com/iterative/shtab
Source0:        %{pypi_source shtab}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(click)
# These enable additional tests:
BuildRequires:  fish
BuildRequires:  zsh
BuildRequires:  tcsh

%description
Automatically generate shell tab completion scripts for Python CLI apps.

%package -n     python3-shtab
Summary:        %{summary}

%description -n python3-shtab
Automatically generate shell tab completion scripts for Python CLI apps.

%prep
%autosetup -n shtab-%{version}
# remove coverage test config
sed -i -e 's/addopts =/#addopts =/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files --assert-license shtab

# Pre-generate and install completion files for shtab itself. It seems that
# there is not a reasonable way to install tcsh completions system-wide.
while read -r shell target
do
  install --directory "%{buildroot}$(dirname "${target}")"
  %{py3_test_envvars} '%{buildroot}%{_bindir}/shtab' \
      --print-own-completion "${shell}" > "%{buildroot}${target}"
done <<'EOF'
bash %{bash_completions_dir}/shtab
zsh %{zsh_completions_dir}/_shtab
fish %{fish_completions_dir}/shtab.fish
EOF

%check
# -rs: print reasons why some tests are skipped
%pytest -rs

%files -n python3-shtab -f %{pyproject_files}
%doc README.rst
%{_bindir}/shtab
%{bash_completions_dir}/shtab
%{zsh_completions_dir}/_shtab
%{fish_completions_dir}/shtab.fish

%changelog
%autochangelog
