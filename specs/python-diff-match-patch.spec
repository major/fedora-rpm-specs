Name:          python-diff-match-patch
Version:       20241021
Release:       %autorelease
Summary:       Algorithms for synchronizing plain text

%global forgeurl https://github.com/diff-match-patch-python/diff-match-patch
%global tag v%{version}
%forgemeta

License:       Apache-2.0
URL:           %forgeurl
Source:        %forgesource

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3dist(pytest)

%global _description %{expand:
The Diff Match and Patch libraries offer robust algorithms to perform
the operations required for synchronizing plain text.

1. Diff
 - Compare two blocks of plain text and efficiently return a list of
   differences.
2. Match
 - Given a search string, find its best fuzzy match in a block of plain
   text. Weighted for both accuracy and location.
3. Patch
 - Apply a list of patches onto plain text. Use best-effort to apply
   patch even when the underlying text doesn't match.

Google's Diff Match and Patch library, packaged for modern Python.}

%description %_description

%package -n python3-diff-match-patch
Summary:       %{summary}

%description -n python3-diff-match-patch %_description


%prep
%forgeautosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install
%if 0%{?fedora} < 43
%pyproject_save_files -L diff_match_patch
%else
%pyproject_save_files -l diff_match_patch
%endif


%check
%pytest -r fEs


%files -n python3-diff-match-patch -f %{pyproject_files}
%if 0%{?fedora} < 43
%license LICENSE
%endif
%doc README.md CHANGELOG.md


%changelog
%autochangelog
