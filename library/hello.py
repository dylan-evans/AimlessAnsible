from ansible.module_utils.basic import AnsibleModule

def run_module():
    mod_args = {
        "name": {"type": str, "required": True}
    }

    result = {
        "changed": False,
        "original_message": "",
        "message": "",
    }

    module = AnsibleModule(argument_spec=mod_args, supports_check_mode=False)

    result["original_message"] = module.params["name"]
    result["message"] = f"Hello, {module.params['name']}!"
    module.exit_json(**result)


if __name__ == '__main__':
    run_module()
