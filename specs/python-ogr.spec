Name:           python-ogr
Version:        0.50.4
Release:        1%{?dist}
Summary:        One API for multiple git forges

License:        MIT
URL:            https://github.com/packit/ogr
Source0:        %{pypi_source ogr}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
One Git library to Rule!

%package -n     python3-ogr
Summary:        %{summary}


%description -n python3-ogr
One Git library to Rule!


%prep
%autosetup -n ogr-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files ogr


%files -n python3-ogr -f %{pyproject_files}
# Epel9 does not tag the license file in pyproject_files as a license. Manually install it in this case
%if 0%{?el9}
%license LICENSE
%endif
%doc README.md


%changelog
* Fri Feb 07 2025 Packit <hello@packit.dev> - 0.50.4-1
- Trigger a new release to confirm the correct SPDX licence.
- Resolves: rhbz#2336934

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.50.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 10 2025 Packit <hello@packit.dev> - 0.50.3-1
- We have improved wrapping of the forge-specific exceptions, string representation of the original exception is now included. (#884)
- The test suite for parsing git URLs has been extended and also the handling of GitHub repository with changed owner or name has been improved. (#874)

* Sat Oct 26 2024 Packit <hello@packit.dev> - 0.50.2-1
- There is a new method for getting a single commit comment, supporting also retrieval and adding reactions in GitHub. (#865)
- Resolves: rhbz#2321974

* Fri Oct 11 2024 Packit <hello@packit.dev> - 0.50.1-1
- We have fixed an issue that caused inconsistencies with the expected behavior stated by the documentation when adding duplicate reactions to GitLab comments. (#861)
- Resolves: rhbz#2318010

* Mon Sep 16 2024 Packit <hello@packit.dev> - 0.50.0-1
- A new` get_commits` method was implemented for GitHub and Gitlab projects. (#857)
- An issue with silently ignoring error (#760) was fixed. (#855)
- Resolves: rhbz#2312527

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.49.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.49.2-2
- Rebuilt for Python 3.13

* Fri Mar 08 2024 Packit <hello@packit.dev> - 0.49.2-1
- `GitLabProject.get_file_content` can now correctly handle file paths starting with `./`. (#844)
- Resolves rhbz#2268584

* Mon Feb 12 2024 Packit <hello@packit.dev> - 0.49.1-1
- Interface for labels was unified and `labels` property for PullRequest and Issue now return list of PRLabel and IssueLabel respectively. (#839)
- Resolves rhbz#2260529

* Sat Jan 27 2024 Packit <hello@packit.dev> - 0.49.0-1
- For Pagure there are 2 new methods available: one for getting users with specified access rights and one for getting members of a group. (#834)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.48.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.48.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 08 2024 Packit <hello@packit.dev> - 0.48.1-1
- Fix log level and wording when Pagure returns an error while retrieving Pagure PR diffstats.
- Resolves rhbz#2257242

* Thu Dec 21 2023 Packit <hello@packit.dev> - 0.48.0-1
- There is a new get_pr_files_diff method supported for Pagure. (#826)
- We have fixed a bug that GithubRelease.url returned an API URL. (#824)
- Resolves rhbz#2255524

* Mon Oct 30 2023 Packit <hello@packit.dev> - 0.47.1-1
- Fixed an issue where getting a list of GitLab merge requests using `.list()` would return only 20 items. (#819)
- Resolves rhbz#2246994

* Wed Oct 11 2023 Packit <hello@packit.dev> - 0.47.0-1
- Added support for removing users/groups from a project and possibility to check for groups with permissions to modify a PR. (#815)
- Resolves rhbz#2125279

* Fri Oct 06 2023 Packit <hello@packit.dev> - 0.46.2-1
- Added missing README to package metadata.

* Fri Sep 08 2023 Packit <hello@packit.dev> - 0.46.0-1
- We have fixed a bug in `get_fork` method for Pagure about checking the usernames for a match when going through existing forks. (#800)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.45.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.45.0-2
- Rebuilt for Python 3.12

* Mon Jun 05 2023 Packit <hello@packit.dev> - 0.45.0-1
- OGR now supports PyGithub >= 1.58.

* Sun Mar 05 2023 Packit <hello@packit.dev> - 0.44.0-1
- OGR now understands a few community-hosted GitLab instances that could not be determined automatically from the hostname. Thanks to that, you don't need to hardcode these instances to be mapped correctly. (#775)

* Thu Feb 23 2023 Packit <hello@packit.dev> - 0.43.0-1
- Fixes an issue with project->service mapping where the service with an url not containing the service type wasn't matched. (#771)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Packit <hello@packit.dev> - 0.42.0-1
- A bug in ogr resulting in returning only first page of pull requests for Pagure has been fixed. (#761)
- ogr now raises `GitForgeInternalError` rather than `PagureAPIException` when getting 50x response from the Pagure API. (#762)

* Thu Oct 27 2022 Packit <hello@packit.dev> - 0.41.0-1
- `CommitComment.comment` has been deprecated in favour of `CommitComment.body` to make the naming consistent across objects. (#748)
- ogr now requires Python 3.9 or later. (#746)

* Fri Sep 16 2022 Packit <hello@packit.dev> - 0.40.0-1
- Using the method `users_with_write_access` you can generate the set of users that have write access to the project and the method `has_write_access(user)` you can find out if the user has write access to the project. (#742)

* Thu Sep 08 2022 Packit <hello@packit.dev> - 0.39.0-1
- We have implemented the `closed_by` property for the Pagure pull request for getting the login of the account that closed the pull request. (https://github.com/packit/ogr/pull/718)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.38.1-2
- Rebuilt for Python 3.11

* Fri Apr 29 2022 Packit <hello@packit.dev> - 0.38.1-1
- When using Tokman as GitHub authentication mechanism, ogr will now raise GithubAppNotInstalledError instead of failing with generic GithubAPIException when app providing tokens is not installed on the repository.
- Use the standard library instead of setuptools for getting the version on Python 3.8+,
  or a smaller package on older Pythons.
  This also fixes the packaging issue with missing `pkg_resources`.

* Thu Apr 28 2022 Packit <hello@packit.dev> - 0.38.0-1
- ogr now correctly raises `OgrException` when given invalid URL to
  `PagureService.get_project_from_url`. (#705)
- We have fixed a bug in ogr that caused `IssueTrackerDisabled` being raised
  only when trying to create an issue on git project with disabled issue
  tracker. Now it is also raised when getting a specific issue or
  an issue list. (#703)

* Thu Mar 31 2022 Packit <hello@packit.dev> - 0.37.0-1
- We have added a new optional parameter, `namespace`, to the `fork_create` method on Git projects, which allows you to
  fork a project into a specific namespace. (Forking to namespaces is not allowed on Pagure.) (#685)
- We have implemented a `get_contributors` function that can be used to get the contributors of a GitHub
  (set of logins) and GitLab (set of authors) project. (#692)
- We have introduced a new exception class `GitForgeInternalError` that indicates a failure that happened within the forge
  (indicated via 50x status code). `\*APIException` have been given a new superclass `APIException` that provides status
  code from forge (in case of error, invalid operation, etc.). (#690)
- We have added a new property to git projects, `has_issues`, that indicates whether project has enabled issues or not.
  Following up on the property, `create_issue` now raises `IssueTrackerDisabled` when the project doesn't have issues
  enabled. (#684)

* Tue Mar 22 2022 Frantisek Lachman <flachman@redhat.com> - 0.36.0-2
- rebuilt

* Wed Mar 16 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 0.36.0-1
- `Release` class has been reworked and `create_release` has been made part of the API for `GitProject`. (#670)
- Factory method for acquiring project or service class from URL has been improved by checking just the hostname for determining the service. (#682)

* Tue Mar 08 2022 Frantisek Lachman <flachman@redhat.com> - 0.35.0-4
- rebuilt

* Wed Feb 23 2022 Frantisek Lachman <flachman@redhat.com> - 0.35.0-3
- rebuilt

* Wed Feb 23 2022 Frantisek Lachman <flachman@redhat.com> - 0.35.0-2
- rebuilt

* Wed Feb 16 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 0.35.0-1
- We have added `target_branch_head_commit` property to the `PullRequest`
  class in `ogr` that allows you to get commit hash of the HEAD of the
  target branch (i.e. base, where the changes are merged to).

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 05 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 0.34.0-1
- We have introduced a new function into `ogr` that allows you to get commit SHA of the HEAD of the branch. (#668)
- A list of Gitlab projects provided by `GitlabService.list_projects()` now contains objects with additional metadata. (#667)

* Fri Dec 10 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.33.0-1
- OGR now fully supports getting PR comments by its ID.

* Tue Nov 23 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.32.0-1
- Removal of features which have been marked as deprecated since `0.14.0`.
  - Removal of renamed properties
    - `Comment.comment` -> `Comment.body`
    - `BasePullRequest.project` -> `BasePullRequest.target_project`
  - Removal of methods for accessing issues or pull requests from `GitProject` class.
  - String can no longer be used as commit status, `CommitStatus` is now required.
  - `PullRequest` constructor has been refactored. In order to use static and offline
    representation of a pull request, use `PullRequestReadOnly` instead.
- `GithubCheckRun.app` property has been added for accessing `GithubApp`.

* Wed Oct 27 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.31.0-1
- Ogr now catches internal exceptions from Gitlab and Github and converts them
  to ogr exceptions, GitlabAPIException and GithubAPIException, respectively. A
  new exception, OgrNetworkError, has been introduced for signalling situations
  where a request could not be performed due to a network outage. (#642)
- The documentation was converted to Google-style docstrings. (#646)
- Releases and development builds of ogr are now built in copr projects
  packit/packit-dev and packit/packit-releases. (#644)

* Thu Sep 30 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.30.0-1
- New method to get pull request and issue comments by their comment ID on
  GitHub and GitLab. (#640)

* Thu Sep 16 2021 Packit Service <user-cont-team+packit-service@redhat.com> - 0.29.0-1
- Please check [COMPATIBILITY.md](https://github.com/packit/ogr/blob/main/COMPATIBILITY.md) to see which methods are implemented for
  particular services.
- Ogr now supports reacting to a comment (issue, pull request) with a given
  reaction. It's possible to obtain the reactions and delete them (only when
  reaction is added by using ogr API). (#636)


* Mon Aug 09 2021 Matej Focko <mfocko@redhat.com> - 0.28.0-1
- New upstream release 0.28.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 15 2021 Jiri Popelka <jpopelka@redhat.com> - 0.27.0-1
- New upstream release 0.27.0

* Fri Jun 11 2021 Tomas Tomecek <ttomecek@redhat.com> - 0.26.0-1
- New upstream release 0.26.0

* Tue Jun 01 2021 Laura Barcziova <lbarczio@redhat.com> - 0.25.0-1
- New upstream release 0.25.0

* Tue Apr 27 2021 Matej Mužila <mmuzila@redhat.com> - 0.24.1-1
- New upstream release 0.24.1

* Fri Apr 23 2021 Matej Mužila <mmuzila@redhat.com> - 0.24.0-1
- New upstream release 0.24.0

* Thu Mar 18 2021 Jiri Popelka <jpopelka@redhat.com> - 0.23.0-1
- New upstream release 0.23.0

* Fri Feb 19 2021 Matej Focko <mfocko@redhat.com> - 0.21.0-1
- New upstream release 0.21.0

* Thu Feb 04 2021 Matej Focko <mfocko@redhat.com> - 0.20.0-1
- New upstream release 0.20.0

* Thu Jan 07 2021 Tomas Tomecek <ttomecek@redhat.com> - 0.19.0-1
- New upstream release 0.19.0

* Wed Dec 09 2020 Jan Sakalos <sakalosj@gmail.com> - 0.18.1-1
- New upstream release 0.18.1

* Tue Oct 27 2020 Jiri Popelka <jpopelka@redhat.com> - 0.18.0-1
- New upstream release 0.18.0

* Wed Sep 30 2020 Matej Focko <mfocko@redhat.com> - 0.16.0-1
- New upstream release 0.16.0

* Wed Sep 16 2020 Tomas Tomecek <ttomecek@redhat.com> - 0.15.0-1
- New upstream release 0.15.0

* Tue Sep 01 2020 Dominika Hodovska <dhodovsk@redhat.com> - 0.14.0-1
- New upstream release 0.14.0

* Wed Aug 19 2020 Jan Sakalos <sakalosj@gmail.com> - 0.13.1-1
- New upstream release 0.13.1

* Wed Aug 05 2020 Jan Sakalos <sakalosj@gmail.com> - 0.13.0-1
- New upstream release 0.13.0

* Thu Jul 09 2020 Jiri Popelka <jpopelka@redhat.com> - 0.12.2-1
- New upstream release 0.12.2

* Wed May 27 2020 Dominika Hodovska <dhodovsk@redhat.com> - 0.12.1-1
- New upstream release 0.12.1

* Wed May 06 2020 Frantisek Lachman <flachman@redhat.com> - 0.12.0-1
- New upstream release 0.12.0

* Fri Apr 17 2020 Frantisek Lachman <flachman@redhat.com> - 0.11.2-1
- New upstream release 0.11.2

* Wed Apr 01 2020 Jan Sakalos <sakalosj@gmail.com> - 0.11.1-1
- patch release: 0.11.1

* Sat Mar 07 2020 Jiri Popelka <jpopelka@redhat.com> - 0.11.0-1
- New upstream release 0.11.0

* Tue Jan 28 2020 Frantisek Lachman <flachman@redhat.com> - 0.10.0-1
- New upstream release 0.10.0

* Wed Dec 04 2019 Frantisek Lachman <flachman@redhat.com> - 0.9.0-1
- New upstream release 0.9.0

* Mon Sep 30 2019 Frantisek Lachman <flachman@redhat.com> - 0.8.0-1
- New upstream release 0.8.0

* Wed Sep 11 2019 Frantisek Lachman <flachman@redhat.com> - 0.7.0-1
- New upstream release 0.7.0

* Tue Jul 23 2019 Frantisek Lachman <flachman@redhat.com> - 0.6.0-1
- New upstream release 0.6.0

* Fri Jun 28 2019 Frantisek Lachman <flachman@redhat.com> - 0.5.0-1
- New upstream release: 0.5.0

* Tue Jun 11 2019 Jiri Popelka <jpopelka@redhat.com> - 0.4.0-1
- New upstream release: 0.4.0

* Tue May 14 2019 Jiri Popelka <jpopelka@redhat.com> - 0.3.1-1
- patch release: 0.3.1

* Mon May 13 2019 Jiri Popelka <jpopelka@redhat.com> - 0.3.0-1
- New upstream release: 0.3.0

* Wed Mar 27 2019 Tomas Tomecek <ttomecek@redhat.com> - 0.2.0-1
- New upstream release: 0.2.0

* Mon Mar 18 2019 Tomas Tomecek <ttomecek@redhat.com> - 0.1.0-1
- New upstream release: 0.1.0

* Thu Feb 28 2019 Frantisek Lachman <flachman@redhat.com> - 0.0.3-1
- New upstream release 0.0.3

* Tue Feb 26 2019 Tomas Tomecek <ttomecek@redhat.com> - 0.0.2-1
- Initial package.
