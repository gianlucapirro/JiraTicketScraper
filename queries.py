# query that asks for issue description
description = {
    'query': """query {{
                issue(issueIdOrKey: "{KEY}", latestVersion: true, screen: "view") {{
                    id
                viewScreenId 
                fields {{
                        key
                    title
                    editable
                    required
                    autoCompleteUrl
                    allowedValues
                    content
                    renderedContent
                    schema {{
                            custom
                        system
                        configuration {{
                key
            value
        }}

                        items
                        type
                        renderer
                    }}
                    configuration
                }}
                expandAssigneeInSubtasks
                expandAssigneeInIssuelinks
                expandTimeTrackingInSubtasks
                systemFields {{
                        descriptionAdf {{
                            value
                    }}
                    environmentAdf {{
                value
        }}
                }}
                customFields {{
                        textareaAdf {{
                            key
                        value
                    }}
                }}            
                tabs {{
                id
            name
            items {{
                    id
                type
            }}
        }}

        isHybridAgilityProject


        agile {{
                epic {{
                  key
            }},
        }}
            }}

            project(projectIdOrKey: "FR") {{
                    id
                name
                key
                projectTypeKey
                simplified
                avatarUrls {{
                        key
                    value
                }}
                archived
                deleted
            }}
        }}"""
}